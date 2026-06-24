from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 아래와 같이 CORS 미들웨어 설정을 변경해 줍니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # 모든 곳에서 접근할 수 있도록 와일드카드 설정
    allow_credentials=False,  # 와일드카드(*)를 쓸 때는 False로 설정해야 오류가 나지 않습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

class Login(BaseModel):
    userid : str
    password : str

USERID = 'user'
PASSWORD = '1234'

@app.post('/login/')
async def login(login: Login):
    if login.userid != USERID:
        return {'message':'사용자 아이디가 다릅니다'}
    if login.password != PASSWORD:
        return {'message':'비밀번호가 다릅니다'}
    return {'message':'로그인 성공'}