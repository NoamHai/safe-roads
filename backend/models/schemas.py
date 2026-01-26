from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel


# Enums (must match frontend <option value="...">)
class RoadType(str, Enum):
    urban = "urban"
    highway = "highway"


class Weather(str, Enum):
    clear = "clear"
    rain = "rain"
    fog = "fog"


class TimeOfDay(str, Enum):
    day = "day"
    night = "night"


class Lighting(str, Enum):
    daylight = "daylight"
    dark_with_streetlights = "dark_with_streetlights"
    dark_no_streetlights = "dark_no_streetlights"


class Junction(str, Enum):
    no_junction = "no_junction"
    junction = "junction"


class RoadSurface(str, Enum):
    dry = "dry"
    wet = "wet"
    unknown = "unknown"


# Request schema
class PredictRequest(BaseModel):
    road_type: RoadType
    weather: Weather
    time_of_day: TimeOfDay
    lighting: Lighting
    junction: Junction
    road_surface: RoadSurface


# Response schema
class ModelResult(BaseModel):
    probability: float
    risk_percent: int
    breakdown: List[Dict[str, Any]]