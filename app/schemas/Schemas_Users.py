from pydantic import BaseModel

class User(BaseModel):
    # sub: str
    last_requested_time: str | None
    email_verified: str | None
    phone_number_verified: str | None
    old_sub: str | None
    name: str | None
    phone_number: str | None
    nd_requests: str | None
    nm_requests: str | None
    # app_key: str | None
    email: str | None
    enabled: bool | None
    status: str | None
    # created: str | None
    # updated: str | None
    # address: str | None
    # config: dict[str, str] | None

class ShowUser(User):
    sub: str
    app_key: str
    created: str
    updated: str
    class Config():
        orm_mode = True