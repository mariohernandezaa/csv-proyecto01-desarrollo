# CSV Preanalisis de Prueba

CSV Preanalisis de Prueba (CPP) es una aplicación web para explorar archivos CSV antes de comenzar un análisis de datos o un trabajo de aprendizaje automático. Su objetivo es ayudarnos a los estudiantes a entender rápidamente qué contiene un conjunto de datos y qué podrían investigar.

La aplicación mostrará el número de filas y columnas, los tipos de datos detectados y los valores vacíos por columna y por fila. También podrá pedir a un modelo de OpenRouter (sin definir de momento) ideas de preguntas de análisis y sugerencias para tratar los valores ausentes.

El análisis se calcula en Python. El archivo y sus filas no se envían al modelo: el backend solo le proporciona un resumen estadístico. Las recomendaciones serán orientativas y no modificarán los datos.

## Documento de diseño

La [plantilla de documentación en Jupyter](notebooks/plantilla_documentacion.ipynb) presenta la idea del proyecto y organiza los apartados que se desarrollarán poco a poco: objetivos, requisitos, diseño, implementación, pruebas y despliegue. Por ahora, solo la introducción está redactada; el resto son encabezados para completar durante el trabajo.


## Alcance previsto

La primera versión de la aplicación se centrará en cargar un CSV, mostrar un informe básico y presentar sugerencias explicativas. No limpiará los datos automáticamente, no entrenará modelos y no generará gráficos. El tamaño máximo de archivo y otros límites se definirán durante el diseño técnico.