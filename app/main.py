from fastapi import FastAPI
from .models import (
    FeedbackRequestScheme,
    FeedbackResponseScheme,
)


app = FastAPI(
    title="FastAPI Lesson 6"
)


@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }


@app.post("/feedback", response_model=FeedbackResponseScheme)
async def feedback_endpoint(feedback: FeedbackRequestScheme):
    return FeedbackResponseScheme(
        message=f"Feedback received. Thank you, {feedback.username}."
    )
