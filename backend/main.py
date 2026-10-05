from fastapi import FastAPI, File, UploadFile, HTTPException
from starlette.concurrency import run_in_threadpool
from analysis import analizar_csv

app = FastAPI()

@app.post("/api/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="El archivo debe ser CSV")

    try:
        return await run_in_threadpool(analizar_csv, file.file)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"No se pudo leer el CSV: {error}")