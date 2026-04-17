from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    nexus_host: str
    nexus_username: str
    nexus_password: str
    new_username: str
    new_user_password: str


class DeleteUserRequest(BaseModel):
    nexus_host: str
    nexus_username: str
    nexus_password: str
    target_username: str


class ResetUserPasswordRequest(BaseModel):
    nexus_host: str
    nexus_username: str
    nexus_password: str
    target_username: str
    new_user_password: str
