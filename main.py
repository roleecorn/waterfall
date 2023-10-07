from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime
home = Path.cwd()
app = FastAPI()  # 建立一個 Fast API application
app.mount("/image",
          StaticFiles(directory="image"), name="image")
app.mount("/assets",
          StaticFiles(directory="assets"), name="assets")
shops_db = [file.stem for file in (
    home / 'sql').iterdir() if file.is_file() and file.suffix == '.db']


def data_format(df: pd.DataFrame, shop: str = None):
    if not shop:
        raise ValueError
    df['date'] = df['ver'].apply(
        lambda x: datetime.fromtimestamp(x).date())

    df['src'] = df.apply(
        lambda row: f"/image/{shop}/{row['date']}/{row['path']}/{row['imgcode']}",
        axis=1)

    cols_to_drop = [
        'path',
        'imgcode',
        'date',
        'ver',
    ]
    df.drop(cols_to_drop, axis=1, inplace=True)


@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    f = open("home.html", mode="r", encoding="utf8").read()
    return HTMLResponse(content=f, status_code=200)


@app.get("/chart")
def showchart(data: str = ""):
    f = open("chart.html", mode="r", encoding="utf8").read()

    return HTMLResponse(content=f, status_code=200)


@app.get("/waterfall")
def showwaterfall(data: str = ""):
    f = open("img2.html", mode="r", encoding="utf8").read()

    return HTMLResponse(content=f, status_code=200)


@app.get("/dbs")
def dbs():
    global shops_db
    files = {}
    for company in shops_db:
        files[company] = {"name": company, "src": company}
    ret = {
        'status': True,
        'data': files
    }
    return JSONResponse(ret)


@app.get("/search_img")
def imgs(shop: str = "eddiebauer",
         name: str = None,
         ver: int = None,
         price_min: float = None,
         price_max: float = None
         ):
    status = sqlite3.connect(home / "sql" / f"{shop}.db")
    if not ver:
        find_max_ver = f'''
        SELECT MAX(ver)
        FROM {shop}
        '''
        cursor = status.cursor()
        cursor.execute(find_max_ver)
        ver = cursor.fetchone()[0]
        cursor.close()
    query = f"SELECT * FROM {shop} WHERE ver={ver}"
    if name:
        query += f" AND name LIKE '%{name}%'"
    if price_min:
        query += f" AND price >= {price_min}"
    if price_max:
        query += f" AND price <= {price_max}"
    query += " LIMIT 3000"
    df = pd.read_sql_query(query, status)
    data_format(df=df, shop=shop)
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


@app.post("/search")
async def search(data: dict):
    print(data)
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
    search_res = []
    search_type = data['search_type']
    for i in range(len(data['inputs'])):
        company = data['searchCompanys'][i]
        search_term = data['inputs'][i]
        conn = sqlite3.connect(f"{company}.db")
        cursor = conn.cursor()
        find_max_ver = f'''
        SELECT MAX(ver)
        FROM {company}
        '''
        cursor.execute(find_max_ver)
        ver = cursor.fetchone()[0]
        cursor.close
        query = f"SELECT COUNT(*) FROM {company} WHERE price < {search_term} AND ver = {ver}"
        if search_type == "cost":
            query = f'''SELECT COUNT(*) FROM {company}
                        WHERE price < {search_term}
                        AND ver = {ver}'''
        elif search_type == "feature":
            query = f'''SELECT COUNT(*) FROM {company}
                        WHERE path LIKE '%{search_term}%'
                        AND ver = {ver}'''
        elif search_type == "name":
            query = f'''SELECT COUNT(*) FROM {company} 
                        WHERE name LIKE '%{search_term}%'
                        AND ver = {ver}'''
        else:
            return
        # if search_type == "cost":
        #     query = f"SELECT COUNT(*) FROM {company} WHERE price < {search_term} AND ver = {ver}"
        # elif search_type == "feature":
        #     query = f"SELECT COUNT(*) FROM {company} WHERE path LIKE '%{search_term}%' AND ver = {ver}"
        # elif search_type == "name":
        #     query = f"SELECT COUNT(*) FROM {company} WHERE name LIKE '%{search_term}%' AND ver = {ver}"
        # else:
        #     return
        cursor = conn.cursor()
        cursor.execute(query)
        search_res.append(cursor.fetchone()[0])
        cursor.close()
        conn.close()
    color = colors[:len(data['inputs'])]
    for i in range(len(data['inputs'])):
        data['searchCompanys'][i] += '：'
        data['searchCompanys'][i] += str(data['inputs'][i])
    chart_ = {
        'labels': data['searchCompanys'],
        'datasetLabel': search_type,
        'data': search_res,
        'backgroundColor': color,
        'borderWidth': 1,
        'scales_min': 0,
        'scales_max': max(search_res)
    }
    ret = {
        'status': True,
        'data': chart_
    }
    return JSONResponse(ret)
