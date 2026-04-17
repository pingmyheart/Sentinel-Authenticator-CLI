from pydantic import BaseModel


class AddUserToGroupRequest(BaseModel):
    sonarqube_host: str
    sonarqube_token: str
    username: str
    group_name: str


class CreateUserRequest(BaseModel):
    sonarqube_host: str
    sonarqube_token: str
    username: str
    password: str
    group_name: str


class DeleteUserRequest(BaseModel):
    sonarqube_host: str
    sonarqube_token: str
    username: str


class ResetUserPasswordRequest(BaseModel):
    sonarqube_host: str
    sonarqube_token: str
    target_username: str
    new_user_password: str
