from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import pandas as pd
import os
app = FastAPI()  # 建立一個 Fast API application
app.mount("/html5upphantom",
          StaticFiles(directory="html5upphantom"), name="html5upphantom")
app.mount("/assets",
          StaticFiles(directory="assets"), name="assets")

@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    f = open("home.html", mode="r", encoding="utf8").read()
    return HTMLResponse(content=f, status_code=200)


@app.get("/test")
def showwaterfall(data: str = ""):
    f = open("chart.html", mode="r", encoding="utf8").read()

    return HTMLResponse(content=f, status_code=200)


@app.get("/test2")
def showchart(data: str = ""):
    f = open("img2.html", mode="r", encoding="utf8").read()

    return HTMLResponse(content=f, status_code=200)


@app.get("/dbs")
def dbs():
    files = {}
    for company in os.listdir("html5upphantom\images"):
        if "." in company:
            continue
        files[company]={"name": company, "src": company}
    ret = {
        'status': True,
        'data': files
    }
    return JSONResponse(ret)


@app.get("/search_img")
def imgs(dbs: str = "", feature: str = "", name: str = ""):
    status = sqlite3.connect("eddiebauer.db")
    if name:
        qry = f'''
        SELECT * FROM eddiebauer  WHERE name LIKE '%{name}%';
        '''
    elif feature:
        qry = f'''
        SELECT * FROM eddiebauer  WHERE path LIKE '%{feature}%';
        '''
    else:
        qry = "SELECT * FROM eddiebauer "

    df = pd.read_sql_query(qry, status)
    result = df.to_dict('records')
    status.close()
    tmp = 0
    sol = {}
    for item in result:
        sol[str(tmp)] = item
        tmp += 1
    ret = {
        'status': True,
        'data': sol
    }
    return JSONResponse(ret)


@app.get("/chart")
def chart():
    data = [12, 19, 3, 1]
    labels = ["Red", "Green", "Blue", "test"]
    colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf"
    ]
    color = colors[:len(data)]
    chart_ = {
        'labels': labels,
        'datasetLabel': "mychart",
        'data': data,
        'backgroundColor': color,
        'borderWidth': 1
    }
    ret = {
        'status': True,
        'data': chart_
    }
    return JSONResponse(ret)


@app.get("/count_test")
def count_test(search: str):
    conn = sqlite3.connect("eddiebauer.db")
    cursor = conn.cursor()

    query = f"SELECT COUNT(*) FROM eddiebauer WHERE name LIKE '%{search}%'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    ret = {
        'status': True,
        'data': result
    }

    return JSONResponse(ret)


@app.post("/search")
async def search(data: dict):
    print(data)
    # return
    colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf"
    ]
    search_res=[]
    search_type=data['search_type']
    for i in range(len(data['inputs'])):
        company=data['searchCompanys'][i]
        print(company)
        conn = sqlite3.connect(f"{company}.db")
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM {company} WHERE price < {data['inputs'][i]}"
        if search_type=="cost":
            query = f"SELECT COUNT(*) FROM {company} WHERE price < {data['inputs'][i]}"
        elif search_type=="feature":
            query = f"SELECT COUNT(*) FROM {company} WHERE path LIKE '%{data['inputs'][i]}%'"
        elif search_type=="name":
            query = f"SELECT COUNT(*) FROM {company} WHERE name LIKE '%{data['inputs'][i]}%'"
        else :
            pass
        cursor.execute(query)
        search_res.append(cursor.fetchone()[0])
        cursor.close()
        conn.close()
    color = colors[:len(data['inputs'])]
    for i in range(len(data['inputs'])):
        data['searchCompanys'][i]+='：'
        data['searchCompanys'][i]+=str(data['inputs'][i])
    chart_ = {
        'labels': data['searchCompanys'],
        'datasetLabel': "mychart",
        'data': search_res,
        'backgroundColor': color,
        'borderWidth': 1,
        'scales_min' : 0,
        'scales_max' :max(search_res)
    }
    ret = {
        'status': True,
        'data': chart_
    }
    return JSONResponse(ret)
