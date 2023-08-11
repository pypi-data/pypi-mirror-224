import typing

import pydantic


class FileRecordRequest(pydantic.BaseModel):
    """Create, update, or delete request for a file record."""

    bucket: str
    key: str
    version: typing.Optional[str] = None


class DeleteFileRequest(pydantic.BaseModel):
    uri: str


class QueryFilesRequest(pydantic.BaseModel):
    filters: dict[str, typing.Any] = pydantic.Field(default_factory=dict)


class SignedUrlResponse(pydantic.BaseModel):
    url: str
