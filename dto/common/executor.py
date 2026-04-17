from typing import Optional

from pydantic import BaseModel


class ExecutorResponse(BaseModel):
    success: bool = True
    message: Optional[str] = "OK"
    response: Optional[object] = None
