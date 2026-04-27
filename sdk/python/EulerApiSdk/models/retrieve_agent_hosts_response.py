from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.peer_presence import PeerPresence


T = TypeVar("T", bound="RetrieveAgentHostsResponse")


@_attrs_define
class RetrieveAgentHostsResponse:
    """
    Attributes:
        code (float):
        agents (list[PeerPresence]):
        message (str | Unset):
    """

    code: float
    agents: list[PeerPresence]
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "agents": agents,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.peer_presence import PeerPresence

        d = dict(src_dict)
        code = d.pop("code")

        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = PeerPresence.from_dict(agents_item_data)

            agents.append(agents_item)

        message = d.pop("message", UNSET)

        retrieve_agent_hosts_response = cls(
            code=code,
            agents=agents,
            message=message,
        )

        return retrieve_agent_hosts_response
