from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db_connection
from utils.jwt_helper import generate_token


# signup buisness logic
def register_user(full_name, email, password, role):
    """
    Register a new user.
    """

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # check if email already exists/validation

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE email = %s
            """,
            (email,),
        )

        existing_user = cursor.fetchone()

        if existing_user:
            return False, "Email already registered", None

        hashed_password = generate_password_hash(password)

        cursor.execute(
            """
            INSERT INTO users
            (full_name, email, password, role)
            VALUES
            (%s, %s, %s, %s)
            """,
            (full_name, email, hashed_password, role),
        )

        conn.commit()

        return True, "User registered successfully", None

    except Exception as e:
        print(f"Signup error :{e}")

        conn.rollback()

        return False, "Databse connection failed"

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    # login business logic


def login_user(email, password):
    """
    authenticates a user and generate a JWT token
    """

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # find user by email
        cursor.execute(
            """
                SELECT 
                id,
                full_name,
                email,
                password,
                role
                FROM users WHERE email = %s
                """,
            (email,),
        )

        user = cursor.fetchone()

        if not user:
            return False, "Invalid email or password", None

        # unpack tuple
        user_id, full_name, user_email, hashed_password, role = user

        if not check_password_hash(hashed_password, password):
            return False, "Invalid email or password", None

        token = generate_token(user_id=user_id, role=role)

        return True, "Login succesfull", token

    except Exception as e:
        print(f"Login error:{e}")

        return False, "Unable to login.Please try again later", None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
