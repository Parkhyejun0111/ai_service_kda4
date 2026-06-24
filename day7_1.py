from fastapi import FastAPI

# "@"하면 데코레이터 : app이라는 애 먼저하고 나머지 실행해
# google.com:8000/ : 슬래시까지만 치면 [실행]하라는 것

# 요청이 들어오면 /가있는곳에 있는 read_root를 실행해서 결과값을 반환하겠다
app = FastAPI()

# 1. URL 경로는 데코레이터 @app.get() 안에 넣습니다.
@app.get("/")                    #HTTP GET 요청에 대한 루트 경로("/")를 정의
def read_root()->dict:           #루트 경로에 대한 요청을 처리하는 함수, 반환 타입은 dict
    return {'message' : '집에 가고싶어!'}  #클라이언트에게 반환할 JSON 형식의 응답

@app.get('/hello/')
def read_hello():
    return {'id':'Hello world!'}

@app.get('/hello1/')
def calculate_plus():
    return{'result':'5+3=8'}


@app.get('/item/{item_id}/') # item_id : 경로 매개변수
def read_item(item_id:int) -> dict:
    return{'item_id':f'{item_id}번이 입력되었습니다.'}

# 매개변수가 여러개 일 수 있음.
@app.get('/inform/name/{name}/user_id/{user_id}/password/{password}')
def print_idpw(name:str, user_id:str, password:str) -> dict:
    return{'inform':f'{name}님의 ID : {user_id}, 비밀번호 : {password}'}


@app.get('/login/{user}')
def read_login(user:str) -> dict:
    if user == '사용자':
        return {'로그인':'로그인 성공'}
    else:
        return{'로그인':'로그인 실패'}
    
# 쿼리 매개변수
@app.get('/query/')
def read_query(item1:str,item2:str) -> dict:
    return {'query':f'{item1}과 {item2}을(를) 검색합니다.'}



# -- list타입 매개변수
from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

@app.get("/search")
def search_items(
    # tags 변수를 문자열 리스트(List[str]) 타입으로 지정합니다.
    # Query(None)은 이 값이 필수값이 아니며 기본값은 빈 상태라는 뜻입니다.
    tags: Optional[List[str]] = Query(None)
):
    # 만약 사용자가 tags를 아무것도 입력하지 않았다면 빈 리스트를 반환하거나 예외 처리를 합니다.
    if not tags:
        return {"message": "태그를 선택하지 않으셨습니다. 전체 목록을 보여줍니다."}
    
    # 사용자가 입력한 태그 리스트를 그대로 활용해 로직을 처리합니다.
    return {
        "message": f"선택하신 태그 [{', '.join(tags)}]에 대한 검색 결과입니다.",
        "selected_tags": tags,
        "total_tags_count": len(tags)
    }


from fastapi import FastAPI, Query
from typing import List 


app = FastAPI()     #FastAPI 애플리케이션 클래스의 인스턴스를 생성

@app.get("/items/")  #리스트 타입 힌트는 반드시 query()와 함께 사용해야 한다
async def read_items(q:list[int] = Query([])): 
    return {"q : " : q}

