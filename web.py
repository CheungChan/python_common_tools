import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/d/{p:path}")
async def download(p: str):
    return FileResponse(p)


if __name__ == "__main__":
    uvicorn.run("web:app", host="0.0.0.0", port=8002, reload=True)
