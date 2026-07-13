from database import get_db_connection


def create_job(data, user):
    conn = None
    cursor = None

    try:
        # extract data from request
        title = data["title"]
        description = data["description"]
        salary = data["salary"]

        # get recruiter ID from authenticated user
        recruiter_id = user["user_id"]

        # connect to database
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO jobs(title,description,salary,recruiter_id)
        VALUES (%s,%s,%s,%s)
        """,
            (title, description, salary, recruiter_id),
        )
        conn.commit()

        return {
            "success": True,
            "message": "job created succcesfully",
        }

    except Exception as e:
        print(f"error :{e}")

        conn.rollback()

        return {"success": False, "message": "failed to create new job"}

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
