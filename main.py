from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import pandas as pd
app = FastAPI()  # 建立一個 Fast API application
app.mount("/html5upphantom",
          StaticFiles(directory="html5upphantom"), name="html5upphantom")


@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    f = open("home.html", mode="r", encoding="utf8").read()
    return HTMLResponse(content=f, status_code=200)

@app.get("/test2")
def showwaterfall(data: str = ""):
    f = open("img2.html", mode="r", encoding="utf8").read()

    return HTMLResponse(content=f, status_code=200)


@app.get("/dbs")
def dbs():
    data1 = {"name": "bottom", "src": "bottom"}
    data2 = {"name": "Shirts", "src": "Shirts"}
    data3 = {"name": "men", "src": "men"}
    files = {"1": data1, "2": data2,"3": data3}
    ret = {
        'status': True,
        'data': files
    }
    return JSONResponse(ret)

@app.get("/ttttest")
def imgs(dbs: str = "",feature:str="",name:str=""):
    status = sqlite3.connect("eddiebauer.db")
    if name:
        qry = f'''
        SELECT * FROM eddiebauer  WHERE name LIKE '%{name}%';
        '''
    elif  feature :
        qry = f'''
        SELECT * FROM eddiebauer  WHERE path LIKE '%{feature}%';
        '''
    else :
        qry = f"SELECT * FROM eddiebauer "
        
    print(qry)
    df = pd.read_sql_query(qry, status)
    # df = df[~df['path'].str.contains(dbs, na=False)]
    result = df.to_dict('records')
    status.close()
    tmp=0
    sol={}
    for item in result:
        sol[str(tmp)]=item
        tmp+=1
    ret = {
        'status': True,
        'data': sol
    }
    return JSONResponse(ret)

@app.get("/chart")
def chart():

    chart_={
        'labels': ["Red", "Green", "Blue"],
        'datasetLabel': "# of Votes",
        'data': [12, 19, 3],
        'backgroundColor': ["#FF0000", "#00FF00", "#0000FF"],
        'borderWidth': 1
    }
    ret = {
        'status': True,
        'data': chart_
    }
    return JSONResponse(ret)
@app.get("/test")
def showwaterfall(data: str = ""):
    f = open("chart.html", mode="r", encoding="utf8").read()

    return HTMLResponse(content=f, status_code=200)