from database import get_db_connection
from psycopg2.extras import RealDictCursor

# apply job route


def apply_to_job(job_id, user):

    conn = None
    cursor = None

    try:
        candidate_id = user["user_id"]

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        query = """
        INSERT INTO applications(
        job_id,
        candidate_id)
        VALUES(%s,%s
        )

        """
        cursor.execute(query, (job_id, candidate_id))

        conn.commit()

        return {"success": True, "message": "Application submitted"}
    except Exception:
        if conn:
            conn.rollback()

        return {"success": False, "message": "Failed to submit application"}

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


# recruiter views applications


def get_applications(job_id, user):

    conn = get_db_connection
    cursor = conn.cursor()

    query = """"

        SELECT 
        users.name,
        users.email,
        applications.applied_at

        FROM applications

        JOIN users
        ON applications.candidate_id=user.id

        JOIN jobs
        On applications.job_id=jobs.id

        WHERE appliactions.job_id=%s
        AND jobs.recruiter_id=%s

        """
    recruiter_id = user["user_id"]

    cursor.execute(query, (job_id, recruiter_id))

    applications = cursor.fetchall()

    return {"success": True, "applications": applications}
