from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()  # 建立一個 Fast API application
app.mount("/html5upphantom",
          StaticFiles(directory="html5upphantom"), name="html5upphantom")


@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    f = open("home.html", mode="r", encoding="utf8").read()
    return HTMLResponse(content=f, status_code=200)


@app.get("/test")
def showwaterfall(data: str = ""):
    f = open("img.html", mode="r", encoding="utf8").read()

    return HTMLResponse(content=f, status_code=200)


@app.get("/users1/{src}")
async def aimg(src: str):
    # src=src.replace(".","/")
    # src+=".jpg"

    return FileResponse("image/2.jpg")


@app.get("/data")
def imgs(dbs: str = ""):

    data1 = {"src": "users1/2", "title": "main"}
    data2 = {"src": "users1/2"}
    # html5upphantom/images/eddiebauer/women/Accessories/1.jpg
    files = {"1": data1, "2": data2, "3": data1, "4": data2}
    if dbs == '111':
        for i in range(1, 50):
            files[str(i)] = {
            "src": f"html5upphantom/images/eddiebauer/men/Bottoms/{i}.jpg"}
            files[str(i)]["title"] = "Bottoms"
            files[str(i)]["id"] = "men"
        ret = {
        'status': True,
        'data': files
        }
    # if dbs=="111":

        return JSONResponse(ret)
    for i in range(1, 50):
        files[str(i)] = {
            "src": f"html5upphantom/images/eddiebauer/women/Accessories/{i}.jpg"}
        files[str(i)]["title"] = "Accessories"
        files[str(i)]["id"] = "women"
    for i in range(50, 60):
        files[str(i)] = {
            "src": f"html5upphantom/images/eddiebauer/women/Bottoms/Capris/{i-49}.jpg"}
        files[str(i)]["title"] = "Bottoms"
        files[str(i)]["id"] = "women"
    for i in range(60, 110):
        files[str(i)] = {
            "src": f"html5upphantom/images/eddiebauer/men/Bottoms/{i-59}.jpg"}
        files[str(i)]["title"] = "Bottoms"
        files[str(i)]["id"] = "men"
    ret = {
        'status': True,
        'data': files
    }
    # if dbs=="111":

    return JSONResponse(ret)


@app.get("/dbs")
def dbs():


    data1 = {"name": "eby", "src": "111"}
    data2 = {"name": "amz", "src": "222"}
    files = {"1": data1, "2": data2}
    ret = {
        'status': True,
        'data': files
    }
    return JSONResponse(ret)
