"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatevent import ChatEvent, ChatEventTypedDict
from .heartbeatevent import HeartbeatEvent, HeartbeatEventTypedDict
from meibelai.types import BaseModel
from meibelai.utils import FieldMetadata, PathParamMetadata, get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class RunChatStreamRequestTypedDict(TypedDict):
    experience_id: int


class RunChatStreamRequest(BaseModel):
    experience_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


RunChatStreamResponseBodyTypedDict = TypeAliasType(
    "RunChatStreamResponseBodyTypedDict",
    Union[HeartbeatEventTypedDict, ChatEventTypedDict],
)
r"""Successful Response"""


RunChatStreamResponseBody = Annotated[
    Union[
        Annotated[HeartbeatEvent, Tag("ping")], Annotated[ChatEvent, Tag("completion")]
    ],
    Discriminator(lambda m: get_discriminator(m, "event", "event")),
]
r"""Successful Response"""
