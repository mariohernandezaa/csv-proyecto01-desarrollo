# CSV Preanalisis de Prueba

CSV Preanalisis de Prueba (CPP) es una aplicación web para explorar archivos CSV antes de comenzar un análisis de datos o un trabajo de aprendizaje automático. Su objetivo es ayudarnos a los estudiantes a entender rápidamente qué contiene un conjunto de datos y qué podrían investigar.

La aplicación mostrará el número de filas y columnas, los tipos de datos detectados y los valores vacíos por columna y por fila. También podrá pedir a un modelo de OpenRouter (sin definir de momento) ideas de preguntas de análisis y sugerencias para tratar los valores ausentes.

El análisis se calcula en Python. El archivo y sus filas no se envían al modelo: el backend solo le proporciona un resumen estadístico. Las recomendaciones serán orientativas y no modificarán los datos.

## Documento de diseño

La [documentación de diseño en Jupyter](notebooks/plantilla_documentacion.ipynb) está redactada por completo. Incluye:

- Descripción del proyecto, objetivos de aprendizaje y stack tecnológico.
- Estructura del proyecto y requisitos funcionales (RF-01 a RF-08) y no funcionales (RNF-01 a RNF-08).
- Cinco diagramas UML en Mermaid: casos de uso, clases, actividad, secuencia y transición de estados.
- Plan de ejecución por fases, con el progreso de cada una.
- Solución técnica, casos de prueba, guía de ejecución y variables de entorno.

El diseño está escrito, pero la implementación no: solo la Fase 1 está hecha (ver más abajo).


## Alcance previsto

La primera versión de la aplicación se centrará en cargar un CSV, mostrar un informe básico y presentar sugerencias explicativas. No limpiará los datos automáticamente, no entrenará modelos y no generará gráficos. Los límites son propuestas del diseño técnico y pueden cambiar: tamaño máximo de 5 MB, análisis de hasta 5 segundos para ese tamaño y tiempo de espera fijo para la IA.

## Progreso: Fase 1 — entorno y maqueta visual

Esta primera fase prepara el terreno del frontend. No hay lógica real todavía: es solo para dejar claro cómo se van a organizar los componentes antes de programar nada funcional. Útil para que cualquiera que se incorpore al proyecto entienda rápido por dónde empezar.

**Qué hay montado:**
- Proyecto **Vue 3 + Vite** dentro de `frontend/`, creado con el generador oficial (`npm create vite`) y con el boilerplate inicial limpiado a mano (con ayuda de IA para redactar algunas partes repetitivas más rápido).
- De momento es **JavaScript puro**, sin TypeScript. Se añadirá más adelante si decidimos que aporta valor.
- Componentes separados en `frontend/src/components/`, uno por bloque visual de la pantalla:
  - `AppHeader.vue` — título y descripción de la app.
  - `CsvDropzone.vue` — zona para arrastrar/seleccionar el CSV (solo visual, no sube nada todavía).
  - `SummaryPanel.vue` — tarjetas de filas, columnas, tipos detectados y valores vacíos (con `—` de relleno, sin datos reales).
  - `SuggestionsPanel.vue` — hueco donde más adelante aparecerán las sugerencias del modelo de IA.
- `frontend/src/styles/main.css` centraliza tipografía, colores (incluye modo oscuro) y estilos base, para no repetir estilos sueltos dentro de cada componente.

**Qué NO hay todavía (a propósito):**
- Nada de lógica: no se lee el CSV, no se calcula nada.
- Nada de TypeScript.
- Nada de backend (Python/FastAPI) ni llamadas a ningún modelo.
- Nada de despliegue (Vercel).

**Cómo arrancarlo en local:**
```bash
cd frontend
npm install
npm run dev
```
Y abrir `http://localhost:5173` en el navegador.

**Siguientes pasos sugerido por IA** (para ir repartiéndolos entre los dos):
1. Decidir y montar el backend en Python que calcule el resumen del CSV (filas, columnas, tipos, vacíos).
2. Conectar `CsvDropzone.vue` para que realmente lea un archivo y lo envíe al backend.
3. Pintar los datos reales en `SummaryPanel.vue` en lugar de los placeholders.
4. Integrar el modelo de IA para las sugerencias de `SuggestionsPanel.vue`.
5. Valorar si merece la pena pasar el frontend a TypeScript antes de que crezca mucho.

## Ejecución con Docker (backend + frontend juntos)

Todo el proyecto (API de FastAPI y la interfaz de Vue ya compilada y servida con Nginx) se levanta con un único comando usando Docker Compose. Nginx sirve los ficheros estáticos del frontend y reenvía las peticiones a `/api` al contenedor del backend, así que no hace falta configurar CORS ni URLs distintas entre ambos.

**Requisitos:** Docker y Docker Compose instalados.

**Configurar la clave de OpenRouter (opcional, solo para sugerencias de IA reales):**
```bash
cp .env.example .env
# Editar .env y rellenar OPENROUTER_API_KEY
```
Si no se configura, la aplicación funciona igual: el informe del CSV se calcula siempre, y `/api/sugerencias` devuelve un error controlado (503) en lugar de sugerencias de IA.

**Arrancar todo:**
```bash
docker compose up --build
```
- Frontend: http://localhost:8080
- Backend (API): http://localhost:8000 (documentación interactiva en `/docs`)

**Parar todo:**
```bash
docker compose down
```
(o `Ctrl+C` si se dejó `docker compose up` en primer plano; ambos contenedores se detienen juntos).

**Reconstruir imágenes tras cambiar dependencias:**
```bash
docker compose up --build
```