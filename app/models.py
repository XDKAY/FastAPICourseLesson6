from pydantic import BaseModel


class FeedbackRequestScheme(BaseModel):
    username: str
    message: str


class FeedbackResponseScheme(BaseModel):
    message: str
