import jwt
import datetime
from config import SECRET_KEY


def generate_token(user_id, role):
    """
    Generate a JWT token for an authenticated user.
    Args:
        user_id(int):Unique ID of the user.
        role(str): User role (candidate or recruiter).

    Returns :
        str: JWT token.
    """

    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token
