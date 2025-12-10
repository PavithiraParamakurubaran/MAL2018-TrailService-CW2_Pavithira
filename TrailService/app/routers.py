from fastapi import APIRouter
from app.models import TrailCreate, TrailUpdate
from app import crud


router = APIRouter(prefix="/trails", tags=["Trails"])


@router.post("/")
def create_trail(trail: TrailCreate):
    return crud.create_trail(trail)


@router.get("/")
def get_trails():
    return crud.get_all_trails()


@router.get("/{trail_id}")
def get_trail(trail_id: int):
    return crud.get_trail_by_id(trail_id)


@router.put("/{trail_id}")
def update_trail(trail_id: int, trail: TrailUpdate):
    return crud.update_trail(trail_id, trail)


@router.delete("/{trail_id}")
def delete_trail(trail_id: int):
    return crud.delete_trail(trail_id)
