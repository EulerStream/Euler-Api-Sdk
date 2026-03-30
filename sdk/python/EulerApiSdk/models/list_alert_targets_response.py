from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_target import AlertTarget


T = TypeVar("T", bound="ListAlertTargetsResponse")


@_attrs_define
class ListAlertTargetsResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        targets (list[AlertTarget] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    targets: list[AlertTarget] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_target import AlertTarget

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[AlertTarget] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = AlertTarget.from_dict(targets_item_data)

                targets.append(targets_item)

        list_alert_targets_response = cls(
            code=code,
            message=message,
            targets=targets,
        )

        return list_alert_targets_response
