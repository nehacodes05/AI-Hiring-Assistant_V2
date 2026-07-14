from database import get_db_connection
from psycopg2.extras import RealDictCursor


# create job
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


# get job function


def get_jobs(user):

    conn = None
    cursor = None

    try:
        recruiter_id = user["user_id"]

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        query = """
        SELECT id, title, description, salary, created_at
        FROM jobs
        WHERE recruiter_id = %s
        ORDER BY created_at DESC
        """

        cursor.execute(query, (recruiter_id,))

        jobs = cursor.fetchall()

        return {"success": True, "jobs": jobs}

    except Exception:
        if conn:
            conn.rollback()
        return {"success": False, "message": "Failed to fetch jobs"}

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


# update job
def update_job(job_id, data, user):

    conn = None
    cursor = None

    try:
        # Extract updated data
        title = data["title"]
        description = data["description"]
        salary = data["salary"]
        recruiter_id = user["user_id"]

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        UPDATE jobs
        SET title = %s,
            description = %s,
            salary = %s
        WHERE id = %s
        AND recruiter_id = %s
        """

        cursor.execute(query, (title, description, salary, job_id, recruiter_id))

        if cursor.rowcount == 0:
            return {"success": False, "message": "job not found."}

        conn.commit()

        return {"success": True, "message": "Job updated successfully"}

    except Exception:
        if conn:
            conn.rollback()

        return {"success": False, "message": "Failed to update job."}

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


# delete job


def delete_job(job_id, user):

    conn = None
    cursor = None

    try:
        recruiter_id = user["user_id"]
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM jobs
        WHERE id = %s
        AND recruiter_id=%S
        """

        cursor.execute(query, (job_id, recruiter_id))

        if cursor.rowcount == 0:
            print(cursor.rowcount)
            return {"success": False, "message": "Job not found."}

        conn.commit()

        return {"success": True, "message": "Job deleted successfully."}

    except Exception:
        if conn:
            conn.rollback()

        return {"success": False, "message": "Failed to delete job."}

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
