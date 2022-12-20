from typing import Optional
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
app = FastAPI()  # 建立一個 Fast API application


@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    ht = """
    <html>
        <head>
            <title>首頁</title>
        </head>
        <body>
            <input type=\"button\" value=\"連結名稱\" onclick=\"location.href=\'http://localhost:8000/test\'\">
        </body>
    <html>"""
    return HTMLResponse(content=ht, status_code=200)


@app.get("/test")
def showwaterfall(data: str = ""):
    f = open("img.html", mode="r", encoding="utf8").read()
    script_lines = f.split("\n")
    template = "url: '/data?dbs={}',"
    script_lines[61] = template.format(data)
    script_content = "\n".join(script_lines)

    return HTMLResponse(content=script_content, status_code=200)


@app.get("/users1/{src}")
async def aimg(src: str):
    # src=src.replace(".","/")
    # src+=".jpg"

    return FileResponse("image/2.jpg")


@app.get("/data")
def imgs(dbs: str = ""):
    
    data1 = {"src": "users1/2", "title": "main"}
    data2 = {"src": "users1/2"}
    files = {"1": data1, "2": data2, "3": data1, "4": data2}
    ret = {
        'status': True,
        'data': files
    }
    return JSONResponse(ret)


@app.get("/dbs")
def dbs():
    # src=src.replace(".","/")
    # src+=".jpg"

    data1 = {"name": "eby", "src": "http://localhost:8000/test"}
    data2 = {"name": "amz", "src": "http://localhost:8000/"}
    files = {"1": data1, "2": data2}
    ret = {
        'status': True,
        'data': files
    }
    return JSONResponse(ret)
