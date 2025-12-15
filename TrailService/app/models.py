from pydantic import BaseModel
from typing import List, Optional


class TrailPoint(BaseModel):
    latitude: float
    longitude: float
    point_order: int


class TrailCreate(BaseModel):
    name: str
    description: str
    difficulty: str
    length_km: float
    user_id: int
    points: List[TrailPoint]
    features: List[int]


class TrailUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    length_km: Optional[float] = None


class TrailOut(BaseModel):
    trail_id: int
    name: str
    description: str
    difficulty: str
    length_km: float
    points: List[TrailPoint]
    features: List[int]
