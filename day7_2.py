from fastapi import FastAPI, Query
from datetime import date
import random

app = FastAPI()

@app.get("/")                  
def print_message() -> dict:       
    return {'message' : '키움 디지털 아카데미 4기에 오신 것을 환영합니다!',
            '학습_단계': [
                '1단계 : 기본 GET 요청',
                '2단계 : 경로 매개변수',
                '3단계 : 쿼리 매개변수',
                '4단계 : POST요청과 모델',
                '5단계 : 실전 프로젝트'
                ],
            'tip': '/docs에서 API문서를 확인해보세요!'}

@app.get("/hello/{name}")
def say_hello(name: str) -> dict:
    today_date = str(date.today())
    lucky_num = random.randint(1, 100)
    
    return {
        'message': f"반갑습니다, {name}님!",
        'today': today_date,
        'lucky_number': lucky_num
    }


@app.get('/grade/{subject}/{score}')
def grade_score(subject: str, score: int) -> dict:  # 1. score를 int(정수)로 변경
    
    # 기본 코멘트 지정 (A학점용)
    comment = "참 잘하셨어요!" 
    
    # 2. 등호를 = 1개로 변경하여 변수에 값 저장
    if score >= 95:
        credit = 'A+'
        comment = '최고에요! 최고학점이네요'  # A+일 때 코멘트 갱신
    else:
        credit = "A"

    return {
        'subject': subject,
        'score': score,
        'credit': credit,
        'comment': comment  # 3. 따옴표를 떼어내서 진짜 변수 값을 매핑
    }



    # ===================pydantic=========

from pydantic import BaseModel

class Item(BaseModel):
        subject : str
        score : int

@app.post('/score/')
def read_score(item:list[Item]):
    return item