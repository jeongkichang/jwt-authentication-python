# jwt-authentication-python
Python study<br/><br/>

세 개의 패키지가 필요합니다.
1. fastapi : 웹프레임워크
2. uvicorn : ASGI 서버
3. pyjwt : JWT 처리

프로젝트에 패키지를 세팅하기 위해서는 가상 환경 설정이 필요합니다.
```bash
python -m venv myenv
source myenv/bin/activate
```

위의 설정을 진행하고, 필요한 패키지는 requirements.txt 파일을 통해 한번에 다운로드가 가능합니다.
```bash
pip install -r requirements.txt
```
<br/>

서버 구동은 아래와 같이 진행하시면 됩니다.
```bash
uvicorn main:app --reload
```
<br/>

curl을 통해 두 개의 앤드포인트로 JWT 토큰 생성 및 유효한지 검증이 가능합니다.
```
# 토큰 생성
curl -X POST "http://127.0.0.1:8000/token"

# 유효한지 검증
curl -X GET "http://127.0.0.1:8000/protected" -H "Authorization: Bearer <your_jwt_token>"
```
