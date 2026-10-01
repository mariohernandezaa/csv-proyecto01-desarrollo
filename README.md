# CSV Preanalisis de Prueba

CSV Preanalisis de Prueba (CPP) es una aplicación web para explorar archivos CSV antes de comenzar un análisis de datos o un trabajo de aprendizaje automático. Su objetivo es ayudarnos a los estudiantes a entender rápidamente qué contiene un conjunto de datos y qué podrían investigar.

La aplicación mostrará el número de filas y columnas, los tipos de datos detectados y los valores vacíos por columna y por fila. También podrá pedir a un modelo de OpenRouter (sin definir de momento) ideas de preguntas de análisis y sugerencias para tratar los valores ausentes.

El análisis se calcula en Python. El archivo y sus filas no se envían al modelo: el backend solo le proporciona un resumen estadístico. Las recomendaciones serán orientativas y no modificarán los datos.

## Documento de diseño

La [plantilla de documentación en Jupyter](notebooks/plantilla_documentacion.ipynb) presenta la idea del proyecto y organiza los apartados que se desarrollarán poco a poco: objetivos, requisitos, diseño, implementación, pruebas y despliegue. Por ahora, solo la introducción está redactada; el resto son encabezados para completar durante el trabajo.


## Alcance previsto

La primera versión de la aplicación se centrará en cargar un CSV, mostrar un informe básico y presentar sugerencias explicativas. No limpiará los datos automáticamente, no entrenará modelos y no generará gráficos. El tamaño máximo de archivo y otros límites se definirán durante el diseño técnico.

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