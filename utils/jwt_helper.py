import jwt
import datetime
from config import SECRET_KEY


# generating jwt
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


# implementing jwt verification
def verify_token(token):
    """
    verifies a jwt token.
    args :
         token(str):JWT recieved from the client.
     returns :
          dict : Decode payload if the token is valid.
    """

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        return payload

    except jwt.ExpiredSignatureError:
        raise

    except jwt.InvalidTokenError:
        raise
