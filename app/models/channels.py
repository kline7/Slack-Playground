from pydantic import BaseModel, Field
from typing import Optional, Any


class Topic(BaseModel):
    value: str = Field(...)
    creator: str = Field(...)
    last_set: int = Field(...)


class Channel(BaseModel):
    id: str = Field(..., description="Identifier of channel")
    name: str = Field(..., description="Name of the channel")
    is_channel: bool = Field(...)
    is_group: bool = Field(...)
    is_im: bool = Field(...)
    is_mpim: bool = Field(...)
    is_private: bool = Field(...)
    created: int = Field(..., description="timestamp of creation")
    is_archived: bool = Field(...)
    is_general: bool = Field(...)
    unlinked: int = Field(...)
    name_normalized: str = Field(...)
    is_shared: bool = Field(...)
    is_org_shared: bool = Field(...)
    is_pending_ext_shared: bool = Field(...)
    pending_shared: list = Field(...)
    context_team_id: str = Field(..., description="Unique identifier of the team")
    updated: int = Field(..., description="timestamp of update")
    parent_conversation: Optional[Any] = Field(...)
    creator: str = Field(...)
    is_ext_shared: bool = Field(...)
    shared_team_ids: list = Field(...)
    pending_connected_team_ids: list = Field(...)
    is_member: bool = Field(...)
    topic: Topic = Field(...)
    purpose: Topic = Field(...)
    previous_names: list = Field(...)
    num_members: int = Field


class Channels(BaseModel):
    channels: list[Channel]
