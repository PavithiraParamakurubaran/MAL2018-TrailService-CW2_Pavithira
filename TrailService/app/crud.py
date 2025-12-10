from app.database import create_connection
from app.models import TrailCreate, TrailUpdate

# --- Trail CRUD ---

def create_trail(trail: TrailCreate):
    conn = create_connection()
    cursor = conn.cursor()

    # Insert trail
    cursor.execute(
        "EXEC sp_InsertTrail ?, ?, ?, ?, ?",
        trail.name,
        trail.description,
        trail.difficulty,
        trail.length_km,
        trail.user_id
    )
    conn.commit()

    # Get last inserted TrailId (assuming SQL Server SCOPE_IDENTITY)
    cursor.execute("SELECT SCOPE_IDENTITY()")
    trail_id = int(cursor.fetchone()[0])

    # Insert TrailPoints
    for point in trail.points:
        cursor.execute(
            "EXEC sp_InsertTrailPoint ?, ?, ?, ?",
            trail_id,
            point.latitude,
            point.longitude,
            point.point_order
        )

    # Insert Features (assuming table for trail features)
    for feature_id in trail.features:
        cursor.execute(
            "EXEC sp_InsertTrailFeature ?, ?",
            trail_id,
            feature_id
        )

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Trail created successfully", "trail_id": trail_id}


def get_all_trails():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_GetAllTrails")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_trail_by_id(trail_id: int):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_GetTrailById ?", trail_id)
    row = cursor.fetchone()

    cursor.close()
    conn.close()
    return row


def update_trail(trail_id: int, data: TrailUpdate):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "EXEC sp_UpdateTrail ?, ?, ?, ?, ?",
        trail_id,
        data.name,
        data.description,
        data.difficulty,
        data.length_km
    )

    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Trail updated successfully"}


def delete_trail(trail_id: int):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_DeleteTrail ?", trail_id)
    conn.commit()

    cursor.close()
    conn.close()
    return {"message": "Trail deleted successfully"}
