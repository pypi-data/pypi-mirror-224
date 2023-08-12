#!/usr/bin/env python
# *****************************************************************************
# Copyright (C) 2023 Thomas Touhey <thomas@touhey.fr>
#
# This software is governed by the CeCILL 2.1 license under French law and
# abiding by the rules of distribution of free software. You can use, modify
# and/or redistribute the software under the terms of the CeCILL 2.1 license as
# circulated by CEA, CNRS and INRIA at the following URL: https://cecill.info
#
# As a counterpart to the access to the source code and rights to copy, modify
# and redistribute granted by the license, users are provided only with a
# limited warranty and the software's author, the holder of the economic
# rights, and the successive licensors have only limited liability.
#
# In this respect, the user's attention is drawn to the risks associated with
# loading, using, modifying and/or developing or reproducing the software by
# the user in light of its specific status of free software, that may mean that
# it is complicated to manipulate, and that also therefore means that it is
# reserved for developers and experienced professionals having in-depth
# computer knowledge. Users are therefore encouraged to load and test the
# software's suitability as regards their requirements in conditions enabling
# the security of their systems and/or data to be ensured and, more generally,
# to use and operate it in the same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL 2.1 license and that you accept its terms.
# *****************************************************************************
"""Message queue related utilities for TeaL."""

from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import datetime
from enum import Enum
from logging import getLogger
from typing import AsyncIterator

from aio_pika import ExchangeType, Message, connect_robust as connect_robust_mq
from aio_pika.abc import AbstractChannel, AbstractExchange, AbstractQueue

from pydantic import AmqpDsn, BaseModel, BaseSettings, Field

logger = getLogger(__name__)

# ---
# Constants and message formats.
# ---


class CallbackMessage(BaseModel):
    """Body for a callback message in the message queue."""

    url: str
    """Resulting callback URL with parameters and fragment."""

    state: str
    """State for which the callback is emitted."""


class PowensHMACSignature(BaseModel):
    """HMAC signature date for Powens hook body.

    The signature is computed by using the following data::

        BASE_64(
            HMAC_SHA256(
                <METHOD> + "." + <ENDPOINT> + "." + <DATE> + "." + <PAYLOAD>,
                SECRET_KEY
            )
        )

    Where:

    * METHOD is the HTTP method in uppercase.
    * ENDPOINT is the HTTP request path, e.g. "/my-webhook-listener"
    * DATE is the raw "BI-Signature-Date" header.
    * PAYLOAD is the raw webhook data payload.
    """

    signature: str
    """The computed signature on Powens' end."""

    payload_prefix: str
    """The computed prefix to prepend the payload with for computing."""

    signature_date: datetime | None
    """The date and time at which the signature has been produced at."""


class PowensHookMessage(BaseModel):
    """Body for a Powens webhook message in the message queue."""

    domain: str
    """Domain for which the webhook is emitted."""

    hook: str
    """Type of hook for which the webhook is emitted."""

    hmac_signature: PowensHMACSignature | None
    """The HMAC signature, if present."""

    user_token: str | None
    """User scoped token with which the hook is authenticated."""

    payload: str
    """The UTF-8 decoded payload."""


class EventRoutingKey(str, Enum):
    """Routing key for events."""

    CALLBACKS = ('callbacks')
    """An HTTP request has landed on callback endpoints with a known state.

    Messages sent with this routing key will have the
    :py:class:`CallbackMessage` format.
    """

    POWENS_HOOKS = ('powens_hooks')
    """An HTTP request has landed on Powens hook endpoints.

    Messages sent with this routing key will have the
    :py:class:`PowensHookMessage` format.
    """


# ---
# AMQP related utilities.
# ---


class AMQSettings(BaseSettings):
    """RabbitMQ related settings."""

    amqp_dsn: AmqpDsn = Field(env='AMQP_URL')
    """AMQP connection URI to use.

    An example AMQP URI for localhost is the following:

        amqp://rabbitmq:5672/

    See the `RabbitMQ URI Specification`_ for more information.

    .. _RabbitMQ URI Specification: https://www.rabbitmq.com/uri-spec.html
    """

    amqp_exchange_name: str = Field(
        minlength=1,
        default='events',
        env='AMQP_EXCHANGE',
    )
    """Exchange name for events.

    The exchange with this name will be declared as a direct exchange, and
    events will be sent using the routing keys declared in
    :py:class:`EventRoutingKey` depending on the message body.
    """


@asynccontextmanager
async def event_channel_and_exchange(
    *,
    settings: AMQSettings,
) -> AsyncIterator[tuple[AbstractChannel, AbstractExchange]]:
    """Get the event channel and exchange.

    :param settings: The settings to base the connection on.
    """
    connection = await connect_robust_mq(settings.amqp_dsn)
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=0)

        exchange = await channel.declare_exchange(
            settings.amqp_exchange_name,
            ExchangeType.DIRECT,
        )

        yield channel, exchange


@asynccontextmanager
async def event_exchange(
    *,
    settings: AMQSettings,
) -> AsyncIterator[AbstractExchange]:
    """Get the event exchange for sending events.

    :param settings: The settings to base the connection on.
    """
    async with event_channel_and_exchange(settings=settings) as (_, exchange):
        yield exchange


@asynccontextmanager
async def event_queue(
    *,
    settings: AMQSettings,
    routing_keys: tuple[EventRoutingKey, ...] = (
        EventRoutingKey.CALLBACKS,
        EventRoutingKey.POWENS_HOOKS,
    ),
) -> AsyncIterator[AbstractQueue]:
    """Get an exclusive event queue for receiving events.

    :param settings: The settings to base the connection on.
    """
    async with event_channel_and_exchange(
        settings=settings,
    ) as (channel, exchange):
        queue = await channel.declare_queue(exclusive=True)
        for routing_key in routing_keys:
            await queue.bind(exchange, routing_key)

        yield queue


async def send_message(
    message: CallbackMessage | PowensHookMessage, /, *,
    settings: AMQSettings,
    routing_key: EventRoutingKey,
) -> None:
    """Send a message on the message queue."""
    async with event_exchange(settings=settings) as exchange:
        body = message.json(separators=(',', ':')).encode('utf-8')
        logger.info(
            'Sending message to routing key %r with body %r',
            routing_key.value,
            body,
        )
        await exchange.publish(
            Message(body=body),
            routing_key=routing_key,
        )
