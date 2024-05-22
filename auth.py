import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"  # 비밀 키 설정
ALGORITHM = "HS256"  # 사용할 알고리즘 설정
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 토큰 만료 시간 설정

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None
