from fastapi import APIRouter, HTTPException
from app.models import TrailCreate, TrailUpdate
from app import crud

router = APIRouter(prefix="/trails", tags=["Trails"])


@router.post("/")
def create_trail(trail: TrailCreate):
    result = crud.create_trail(trail)

    if result is None:
        raise HTTPException(
            status_code=500,
            detail="Failed to create trail"
        )

    return result


@router.get("/")
def get_trails():
    return crud.get_all_trails()


@router.get("/{trail_id}")
def get_trail(trail_id: int):
    trail = crud.get_trail_by_id(trail_id)

    if trail is None:
        raise HTTPException(
            status_code=404,
            detail="Trail not found"
        )

    return trail


@router.put("/{trail_id}")
def update_trail(trail_id: int, trail: TrailUpdate):
    existing = crud.get_trail_by_id(trail_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Trail not found"
        )

    return crud.update_trail(trail_id, trail)


@router.delete("/{trail_id}")
def delete_trail(trail_id: int):
    existing = crud.get_trail_by_id(trail_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Trail not found"
        )

    return crud.delete_trail(trail_id)
