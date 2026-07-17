from database import get_db_connection
from psycopg2.extras import RealDictCursor
from utils.pdf_helper import extract_text_from_pdf
from services.ai_service import analyze_resume_with_gemini
import traceback


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


# recruiter dashboard ,views applications


def get_job_applications(job_id, user):

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        query = """ 

            SELECT 
            users.full_name,
            users.email,
            applications.score,
            applications.feedback,
            applications.resume_path,
            applications.applied_at

            FROM applications

            JOIN users
            ON applications.candidate_id = users.id

            JOIN jobs
            On applications.job_id=jobs.id

            WHERE applications.job_id=%s
            AND jobs.recruiter_id=%s

            ORDER BY applications.score DESC;

            """
        recruiter_id = user["user_id"]

        cursor.execute(query, (job_id, recruiter_id))

        applications = cursor.fetchall()

        return {"success": True, "applications": applications}

    except Exception as e:
        print(e)
        return {"success": False, "message": "Failed to fetch applications"}

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# upload pdf function


def upload_resume(application_id, resume, user):

    # validate file
    if not resume:
        return {"success": False, "message": "Please upload a resume"}

    # validate file type
    if not resume.filename.lower().endswith(".pdf"):
        return {"success": False, "message": "Only pdf upload is allowed"}

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # generate unique file name
        filename = f"application_{application_id}.pdf"

        # generate filename
        filepath = f"uploads/{filename}"

        # save pdf file
        resume.save(filepath)

        query = """
       UPDATE applications
       SET resume_path=%s

       WHERE id =%s
       """

        cursor.execute(query, (filepath, application_id))

        conn.commit()

        # extracting texts from resume for ai analysis
        resume_text = extract_text_from_pdf(filepath)

        analysis = analyze_resume_with_gemini(resume_text)

        score = analysis.get("score")
        feedback = analysis.get("feedback")

        query = """
       UPDATE applications
       SET score=%s,
       feedback=%s
    

       WHERE id =%s
       """

        cursor.execute(query, (score, feedback, application_id))

        conn.commit()

        return {"success": True, "message": "Resume uploaded and analysed succesfully."}

    except Exception as e:
        traceback.print_exc()
        if conn:
            conn.rollback()

        return {"success": False, "message": "failed to upload resume,try again later"}

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# download uploaded resume
def download_resume(application_id, user):

    conn = None
    cursor = None

    try:
        conn = get_db_connection()

        cursor = conn.cursor(cursor_factory=RealDictCursor)

        query = """
            SELECT
                applications.resume_path

            FROM applications

            JOIN jobs
            ON applications.job_id = jobs.id

            WHERE applications.id = %s
            AND jobs.recruiter_id = %s
            """
        recruiter_id = user["user_id"]

        cursor.execute(query, (application_id, recruiter_id))

        resume = cursor.fetchone()

        if not resume:
            return {"success": False, "message": "Resume not found or access denied."}

        return {"success": True, "resume_path": resume["resume_path"]}

    except Exception as e:
        print(e)

        return {"success": False, "message": "Failed to fetch resume."}

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
