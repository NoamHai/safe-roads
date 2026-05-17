from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict, Field, model_validator


class PredictRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    @model_validator(mode="before")
    @classmethod
    def _normalize_legacy_payload(cls, values):
        if not isinstance(values, dict):
            return values

        if any(key in values for key in {"road_type", "weather", "time_of_day", "lighting", "junction", "road_surface"}):
            normalized = dict(values)
            time_of_day = str(values.get("time_of_day", "")).strip().lower()
            lighting = str(values.get("lighting", "")).strip().lower()
            weather = str(values.get("weather", "")).strip().lower()
            road_type = str(values.get("road_type", "")).strip().lower()
            junction = str(values.get("junction", "")).strip().lower()
            road_surface = str(values.get("road_surface", "")).strip().lower()

            normalized.setdefault("SHAA", "12:00" if time_of_day == "day" else "22:00")
            normalized.setdefault("HODESH_TEUNA", 1)
            normalized.setdefault("YOM_BASHAVUA", "לא ידוע")
            normalized.setdefault("SUG_TEUNA", "לא ידוע")
            normalized.setdefault("ROAD_STRUCTURE", "לא ידוע")
            normalized.setdefault("ROHAV", "לא ידוע")
            normalized.setdefault("NAFA", "לא ידוע")
            normalized.setdefault(
                "ZURAT_ISHUV",
                "עירוני" if road_type in {"urban", "city"} else ("כפרי" if road_type in {"rural"} else "לא ידוע"),
            )
            normalized.setdefault("MEHIRUT_MUTERET", "לא ידוע")
            normalized.setdefault(
                "TEURA",
                "אור יום"
                if lighting in {"daylight", "day"} or time_of_day == "day"
                else ("לילה עם תאורה" if lighting == "night_with_lighting" else ("לילה ללא תאורה" if lighting == "night_without_lighting" else "לא ידוע")),
            )
            normalized.setdefault(
                "SUG_DEREH",
                "עירוני בצומת"
                if road_type in {"urban", "city"} and junction not in {"no_junction", "false", "0"}
                else (
                    "עירוני לא בצומת"
                    if road_type in {"urban", "city"}
                    else ("לא עירוני בצומת" if road_type == "rural" and junction not in {"no_junction", "false", "0"} else ("לא עירוני לא בצומת" if road_type == "rural" else "לא ידוע"))
                ),
            )
            normalized.setdefault("SIMUN_TIMRUR", "לא ידוע")
            normalized.setdefault("TKINUT", "לא ידוע")
            normalized.setdefault(
                "PNE_KVISH",
                "יבש" if road_surface == "dry" else ("רטוב ממים" if road_surface == "wet" else ("מכוסה בבוץ" if road_surface == "mud" else ("מרוח בחומר דלק" if road_surface == "fuel" else "לא ידוע"))),
            )
            normalized.setdefault(
                "MEZEG_AVIR",
                "בהיר" if weather == "clear" else ("מעונן" if weather == "cloudy" else ("גשום" if weather == "rainy" else ("ערפילי" if weather == "foggy" else "לא ידוע"))),
            )
            normalized.setdefault("YOM_LAYLA", "יום" if time_of_day == "day" else ("לילה" if time_of_day == "night" else "לא ידוע"))
            return normalized

        return values

    SHAA: int | str = Field(...)
    HODESH_TEUNA: int | str = Field(...)
    YOM_BASHAVUA: int | str = Field(...)
    SUG_TEUNA: int | str = Field(...)
    ROAD_STRUCTURE: int | str = Field(...)
    ROHAV: int | str = Field(...)
    NAFA: int | str = Field(...)
    ZURAT_ISHUV: int | str = Field(...)
    MEHIRUT_MUTERET: int | str = Field(...)
    TEURA: int | str = Field(...)
    SUG_DEREH: int | str = Field(...)
    SIMUN_TIMRUR: int | str = Field(...)
    TKINUT: int | str = Field(...)
    PNE_KVISH: int | str = Field(...)
    MEZEG_AVIR: int | str = Field(...)
    YOM_LAYLA: int | str = Field(...)


# Response schema
class ModelResult(BaseModel):
    probability: float
    risk_percent: int
    breakdown: List[Dict[str, Any]]