from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class UserRead(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


class StreamStartRequest(BaseModel):
    title: str = Field(default="CO-Live session")
    notes: str = Field(default="")


class StreamResponse(BaseModel):
    status: str
    session_id: int | None = None
    message: str
