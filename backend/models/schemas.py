from typing import Any, Dict, List

from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    hour: int = Field(..., ge=0, le=23)
    month: int = Field(..., ge=1, le=12)
    accident_type: int | str
    speed_limit: int | str
    district: int | str | None = None


# Response schema
class ModelResult(BaseModel):
    probability: float
    risk_percent: int
    breakdown: List[Dict[str, Any]]