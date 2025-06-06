"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .metadata import Metadata, MetadataTypedDict
from meibelai.types import BaseModel
from typing_extensions import TypedDict


class UpdateDatasourceRequestTypedDict(TypedDict):
    description: str
    name: str
    type: str
    metadata: MetadataTypedDict


class UpdateDatasourceRequest(BaseModel):
    description: str

    name: str

    type: str

    metadata: Metadata
