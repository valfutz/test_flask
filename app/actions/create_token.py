from datetime import datetime, timedelta
from app.config import SECRET_KEY
import jwt


def create_token(username):
    payload = {
        'username': username,
        'exp': datetime.now() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
