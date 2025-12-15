from app.database import create_connection
from app.models import TrailCreate, TrailUpdate

def create_trail(trail: TrailCreate):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "EXEC sp_InsertTrail ?, ?, ?, ?, ?",
            trail.name,
            trail.description,
            trail.difficulty,
            trail.length_km,
            trail.user_id
        )

        row = cursor.fetchone()
        if row is None or row[0] is None:
            raise Exception("Failed to create trail: no Trail ID returned")

        trail_id = int(row[0])


        conn.commit()

        return {
            "message": "Trail created successfully",
            "trail_id": trail_id
        }

    except Exception as e:
        conn.rollback()
        raise Exception(f"Database error while creating trail: {str(e)}")

    finally:
        cursor.close()
        conn.close()


def get_all_trails():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_GetAllTrails")
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    results = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()
    return results



def get_trail_by_id(trail_id: int):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_GetTrailById ?", trail_id)
    row = cursor.fetchone()

    if row is None:
        cursor.close()
        conn.close()
        return None

    columns = [column[0] for column in cursor.description]
    trail = dict(zip(columns, row))

    cursor.close()
    conn.close()
    return trail



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

    # Fetch the updated trail
    cursor.execute("EXEC sp_GetTrailById ?", trail_id)
    row = cursor.fetchone()
    if row is None:
        cursor.close()
        conn.close()
        return None

    columns = [column[0] for column in cursor.description]
    updated_trail = dict(zip(columns, row))

    cursor.close()
    conn.close()
    return updated_trail


def delete_trail(trail_id: int):
    # Check if the trail exists
    existing_trail = get_trail_by_id(trail_id)
    if not existing_trail:
        return None

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_DeleteTrail ?", trail_id)
    conn.commit()

    cursor.close()
    conn.close()
    return {"message": f"Trail {trail_id} deleted successfully"}

