from typing import Optional

from pydantic import BaseModel


class ActionJacocoReportRequest(BaseModel):
    github_organization: str
    github_token: str
    scan_branch: Optional[str] = None
    jacoco_report_artifact: Optional[str] = None


class CreateRepositoryRequest(BaseModel):
    github_organization: str
    github_token: str
    repository_name: str
    team_name: Optional[str] = None


class CreateTeamReqeust(BaseModel):
    github_organization: str
    github_token: str
    team_name: str
