from fastapi import FastAPI, File, UploadFile, HTTPException, status
from starlette.concurrency import run_in_threadpool # Importamos run_in_threadpool para ejecutar la función analizar_csv en un hilo separado
from analysis import analizar_csv

app = FastAPI()
# 5 MB en bytes
MAX_FILE_SIZE = 5 * 1024 * 1024

@app.post("/api/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="El archivo debe ser CSV")

    if file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="El archivo supera el límite permitido de 5MB."
        )

    try:
        return await run_in_threadpool(analizar_csv, file.file)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"No se pudo leer el CSV: {error}")