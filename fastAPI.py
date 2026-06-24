from fastapi import FastAPI

# "@"하면 데코레이터 : app이라는 애 먼저하고 나머지 실행해
# google.com:8000/ : 슬래시까지만 치면 [실행]하라는 것

# 요청이 들어오면 /가있는곳에 있는 read_root를 실행해서 결과값을 반환하겠다
app = FastAPI()

# 1. URL 경로는 데코레이터 @app.get() 안에 넣습니다.
@app.get("/")
def read_root():  # 2. 함수 괄호 안은 비워두거나 필요한 변수명만 적습니다.
    return {"Hello": "World"}
