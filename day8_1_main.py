import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision
from fastapi import FastAPI,File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np


# 랜더링 : 브라우저 화면에 뭔가를 뿌려준다
# 이 랜더링으로 진자2에서 제공하는 라이브러리 사용할 것

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request,
        'index.html',
        {'name':'박혜준', 'message':'나는야 방케준','age':'28살'}
    )




