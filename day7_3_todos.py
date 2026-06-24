from fastapi import FastAPI, Body
from datetime import date
import random
from typing import Optional


app = FastAPI()

todo_data = {
    1:{'id':1, 'contents': '아침 먹기', 'is_done':True},
    2:{'id':2, 'contents': '점심 먹기', 'is_done':False},
    3:{'id':3, 'contents': '운동 하기', 'is_done':False}
}

# 전체 조회
@app.get('/todos')
def get_todos():
    return list(todo_data.values())

# 특정 id로 조회
@app.get('/todos/{id}')
def get_id_todo(id:int):
    return todo_data.get(id,{})


from pydantic import BaseModel

class Class_Todo(BaseModel):
    id:int
    contents:str
    done:bool


# 일정(데이터) 추가하기
@app.post('/insert_todo/')
def insert_todo(todo:Class_Todo):
    todo_data[todo.id] = todo.model_dump()
    return todo_data[todo.id]


# 특정 데이터 수정하기(true->false,false->true)
@app.patch('/update_todo/{id}')
def update_todo(id:int, is_done:bool=Body(...,embed = True)):   # "..." : mandantory field(반드시 들어와야하는 필드)
    if id in todo_data:
        todo_data[id]['done'] = is_done
        return todo_data[id]
    else:
        return{'message':'해당 ID가 존재하지 않습니다.'}
    


# 특정 데이터 삭제하기
@app.delete('/delete_todo/{id}')
def delete_todo(id:int):
    if id in todo_data:
        todo_data.pop(id, None)
        return todo_data
    else:
        return{'message':'해당 id가 존재하지 않습니다.'}





