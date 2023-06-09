from datetime import datetime, time
from typing import Any, Optional

from pydantic import BaseModel
from pydantic.utils import GetterDict


class UserServiceGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {
            "id",
            "service_type",
            "expected_date",
            "executed_date",
            "start_time",
            "end_time",
            "observations",
            "customer_id",
            "headquarter_id",
            "invoice_id",
        }:
            return getattr(self._obj.service, key)
        else:
            return super(UserServiceGetter, self).get(key, default)


class UserService(BaseModel):
    id: Optional[str]
    service_type: Optional[str]
    expected_date: Optional[datetime]
    executed_date: Optional[datetime]
    start_time: Optional[time]
    end_time: Optional[time]
    observations: Optional[str]
    customer_id: Optional[int]
    headquarter_id: Optional[int]
    invoice_id: Optional[int]

    class Config:
        orm_mode = True
        getter_dict = UserServiceGetter


class ServiceUserGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {
            "id",
            "document_id",
            "full_name",
            "email",
            "is_active",
            "is_technician",
            "is_customer",
            "is_superuser",
            "color",
        }:
            return getattr(self._obj.user, key)

        else:
            return super(ServiceUserGetter, self).get(key, default)


class ServiceUser(BaseModel):
    id: str
    document_id: Optional[str]
    full_name: str
    email: str
    is_active: bool
    is_technician: bool
    is_customer: bool
    is_superuser: bool
    color: Optional[str]

    class Config:
        orm_mode = True
        getter_dict = ServiceUserGetter
