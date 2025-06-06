"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from meibelai.types import BaseModel
from meibelai.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class DataTypedDict(TypedDict):
    content: str


class Data(BaseModel):
    content: str


class ChatEventTypedDict(TypedDict):
    r"""A server-sent event containing chat completion content"""

    id: str
    data: DataTypedDict
    event: Literal["completion"]


class ChatEvent(BaseModel):
    r"""A server-sent event containing chat completion content"""

    id: str

    data: Data

    EVENT: Annotated[
        Annotated[Literal["completion"], AfterValidator(validate_const("completion"))],
        pydantic.Field(alias="event"),
    ] = "completion"
