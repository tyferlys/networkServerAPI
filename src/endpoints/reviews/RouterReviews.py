from fastapi import APIRouter

import PIL
from fastapi import APIRouter, HTTPException

from src.database.operations.operationsUsers import createReview
from src.types.UsersRequests import createReviewRequest
from src.types.UsersResponses import UsersCreateResponse


routerReviews = APIRouter()


@routerReviews.post("/")
def create_review(review: createReviewRequest) -> UsersCreateResponse:
    try:
        result = createReview(review)

        return UsersCreateResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ошибка при создании")