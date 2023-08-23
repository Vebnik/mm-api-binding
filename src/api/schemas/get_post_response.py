from pydantic import BaseModel


class GetPostResponse(BaseModel):
    root_id: str | None = ''