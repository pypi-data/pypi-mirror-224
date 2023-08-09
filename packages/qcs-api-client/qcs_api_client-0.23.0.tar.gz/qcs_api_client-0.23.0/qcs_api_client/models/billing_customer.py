from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

import attr

from ..types import UNSET
from ..util.serialization import is_not_none

T = TypeVar("T", bound="BillingCustomer")


@attr.s(auto_attribs=True)
class BillingCustomer:
    """A representation of a QCS's account billing customer. Note, `balance` does not account for the upcoming invoice.

    Attributes:
        email (str):
        id (str):
    """

    email: str
    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        email = self.email
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "id": id,
            }
        )

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        id = d.pop("id")

        billing_customer = cls(
            email=email,
            id=id,
        )

        billing_customer.additional_properties = d
        return billing_customer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
