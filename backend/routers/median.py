from fastapi import APIRouter, HTTPException
from models import ArrayRequest
from services.statistics_service import calculate_median

router = APIRouter()

@router.post("/median/")
def median_endpoint(request: ArrayRequest):
    try:
        median = calculate_median(request.array)
        return {"median": median}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))