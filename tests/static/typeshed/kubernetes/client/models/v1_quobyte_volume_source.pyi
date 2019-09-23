# Stubs for kubernetes.client.models.v1_quobyte_volume_source (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1QuobyteVolumeSource:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    group: Any = ...
    read_only: Any = ...
    registry: Any = ...
    user: Any = ...
    volume: Any = ...
    def __init__(self, group: Optional[Any] = ..., read_only: Optional[Any] = ..., registry: Optional[Any] = ..., user: Optional[Any] = ..., volume: Optional[Any] = ...) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    @property
    def registry(self): ...
    @registry.setter
    def registry(self, registry: Any) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user: Any) -> None: ...
    @property
    def volume(self): ...
    @volume.setter
    def volume(self, volume: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...