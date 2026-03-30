from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.peer_presence_type import PeerPresenceType
from ..models.peer_role import PeerRole

T = TypeVar("T", bound="PeerPresence")


@_attrs_define
class PeerPresence:
    """
    Attributes:
        last_seen (float):
        role (PeerRole):
        id (str):
        type_ (PeerPresenceType):
    """

    last_seen: float
    role: PeerRole
    id: str
    type_: PeerPresenceType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_seen = self.last_seen

        role = self.role.value

        id = self.id

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastSeen": last_seen,
                "role": role,
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_seen = d.pop("lastSeen")

        role = PeerRole(d.pop("role"))

        id = d.pop("id")

        type_ = PeerPresenceType(d.pop("type"))

        peer_presence = cls(
            last_seen=last_seen,
            role=role,
            id=id,
            type_=type_,
        )

        peer_presence.additional_properties = d
        return peer_presence

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
