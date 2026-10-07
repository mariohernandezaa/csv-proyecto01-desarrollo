import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile, status
from pydantic import BaseModel
from starlette.concurrency import run_in_threadpool

from analysis import analizar_csv

load_dotenv(Path(__file__).with_name(".env"))

app = FastAPI()

MAX_FILE_SIZE = 5 * 1024 * 1024
OPENROUTER_BASE_URL = os.getenv(
    "OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1/chat/completions"
)
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/free")


class SugerenciasRequest(BaseModel):
    informe: dict


class SugerenciasResponse(BaseModel):
    preguntas_analisis: list[str]
    tratamientos: list[dict]
    aviso: str


def _build_prompt(informe: dict) -> str:
    """Construye un prompt seguro usando únicamente el resumen estadístico."""
    return f"""
Eres un asistente de análisis de datos para CSV. Utiliza únicamente el resumen
estadístico siguiente. No inventes datos, filas ni valores originales.

RESUMEN CSV:
{json.dumps(informe, ensure_ascii=False, indent=2)}

Tu tarea es proponer:
1. Preguntas concretas de análisis que un estudiante podría investigar.
2. Posibles tratamientos para valores ausentes, vinculados a las columnas.
3. Una advertencia breve de que las recomendaciones son orientativas.

Devuelve exclusivamente un objeto JSON válido con estas propiedades:
- preguntas_analisis: array de strings
- tratamientos: array de objetos con "columna" y "opciones"
- aviso: string

No modifiques el archivo CSV. No describas código. No incluyas texto fuera del
JSON y no inventes información que no aparezca en el resumen.
"""


def _request_openrouter(prompt: str) -> SugerenciasResponse:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OpenRouter no está configurado en el servidor.",
        )

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "Eres un asistente que siempre responde con JSON válido.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,
        "response_format": {"type": "json_object"},
    }

    request = Request(
        OPENROUTER_BASE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": os.getenv("APP_URL", "http://localhost:5173"),
            "X-Title": "CSV Preanálisis",
        },
    )

    try:
        with urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

        content = result["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        return SugerenciasResponse(**parsed)
    except (HTTPError, URLError, KeyError, TypeError, ValueError) as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"No se pudieron obtener sugerencias: {error}",
        ) from error


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


@app.post("/api/sugerencias")
async def sugerencias(payload: SugerenciasRequest):
    """Genera sugerencias mediante OpenRouter usando solo el resumen CSV."""
    try:
        return _request_openrouter(_build_prompt(payload.informe))
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"No se pudieron obtener sugerencias: {error}",
        ) from error