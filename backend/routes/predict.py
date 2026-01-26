from fastapi import APIRouter, HTTPException
from typing import Any, Dict, List
import logging

from ..models.schemas import PredictRequest, ModelResult
from ..services.model_service import predict_probability

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/predict", response_model=ModelResult)
def predict(req: PredictRequest):
    try:
        logger.info(f"=== PREDICTION REQUEST ===")
        logger.info(f"Request data: {req.model_dump()}")
        
        payload = req.model_dump(mode="json")  # Enums -> strings
        logger.info(f"Payload (JSON mode): {payload}")
        
        result = predict_probability(payload)  # returns dict
        logger.info(f"Result: {result}")
        
        response = ModelResult(**result)
        logger.info(f"=== PREDICTION SUCCESS ===")
        return response
    except Exception as e:
        logger.exception("Error occurred during prediction")
        raise HTTPException(status_code=500, detail="Internal server error")