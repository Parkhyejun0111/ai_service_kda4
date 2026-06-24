from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware, #crossoriginresourceshare:다른 오리진에서와도 쉐어해줄거야.
    allow_origins=["http://localhost:5173"],  # React 개발 서버만 허용(허용할 출처)
    allow_credentials=True,  #(인증정보 허용, 쿠키, jWT토큰 등등)
    allow_methods=["*"],     #허용할 HTTP메서드(get, post, patch, put, delete)
    allow_headers=["*"],     #허용할 http헤더(Content-Type, Authorization)
)

class Login(BaseModel):
    userid : str
    password : str

USERID = 'user'
PASSWORD = '1234'

@app.post('/login/')
async def login(login:Login):
    if login.userid != USERID:
        return {'message':'사용자 아이디가 다릅니다'}
    if login.password != PASSWORD:
        return {'message':'비밀번호가 다릅니다'}
    return {'message':'로그인 성공'}