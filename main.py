from typing import Optional
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()  # 建立一個 Fast API application
app.mount("/html5up-phantom", StaticFiles(directory="html5up-phantom"), name="html5up-phantom")

@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    f = open("home.html", mode="r", encoding="utf8").read()
    ht = """
    <html>
        <head>
            <title>首頁</title>
        </head>
        <body>
            <input type=\"button\" value=\"資料展示\" onclick=\"location.href=\'http://localhost:8000/test\'\">
            <input type=\"button\" value=\"模板展示\" onclick=\"location.href=\'http://localhost:8000/html5up-phantom/index.html'\">
        </body>
    <html>"""
    return HTMLResponse(content=f, status_code=200)


@app.get("/test")
def showwaterfall(data: str = ""):
    f = open("img.html", mode="r", encoding="utf8").read()
    script_lines = f.split("\n")
    template = f"url: '/data?dbs={data}',"
    # script_lines[61] = template
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
