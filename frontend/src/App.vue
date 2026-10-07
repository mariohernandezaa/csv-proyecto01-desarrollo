<script setup>
import { ref } from 'vue'
import AppHeader from './components/AppHeader.vue'
import CsvDropzone from './components/CsvDropzone.vue'
import SummaryPanel from './components/SummaryPanel.vue'
import SuggestionsPanel from './components/SuggestionsPanel.vue'

const informe = ref(null)
const resultMessage = ref('')
const errorMessage = ref('')
const suggestions = ref(null)
const suggestionsLoading = ref(false)
const suggestionsError = ref('')

function handleAnalysisStart() {
  informe.value = null
  resultMessage.value = ''
  errorMessage.value = ''
  suggestions.value = null
  suggestionsLoading.value = false
  suggestionsError.value = ''
}

function handleAnalysisSuccess(resultado) {
  informe.value = resultado
  resultMessage.value = `Análisis completado: ${resultado.filas} filas y ${resultado.columnas} columnas.`
}

async function requestSuggestions() {
  if (!informe.value) return

  suggestions.value = null
  suggestionsLoading.value = true
  suggestionsError.value = ''

  try {
    const response = await fetch('/api/sugerencias', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ informe: informe.value }),
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.detail || 'No se pudieron generar las sugerencias')
    }

    suggestions.value = data
  } catch (error) {
    suggestionsError.value =
      error instanceof Error
        ? error.message
        : 'No se pudieron generar las sugerencias'
  } finally {
    suggestionsLoading.value = false
  }
}

function handleAnalysisError(mensaje) {
  informe.value = null
  resultMessage.value = ''
  errorMessage.value = mensaje
}
</script>

<template>
  <div class="app">
    <AppHeader />
    <CsvDropzone
      @analysis-start="handleAnalysisStart"
      @analysis-success="handleAnalysisSuccess"
      @analysis-error="handleAnalysisError"
    />
    <section class="results">
      <div class="results-inner">
        <SummaryPanel
          :informe="informe"
          :result-message="resultMessage"
          :error-message="errorMessage"
        />
        <SuggestionsPanel
          :suggestions="suggestions"
          :loading="suggestionsLoading"
          :error-message="suggestionsError"
          :can-generate="Boolean(informe)"
          @generate-suggestions="requestSuggestions"
        />
      </div>
    </section>
  </div>
</template>

<style scoped>
.app {
  width: 100%;
  min-height: 100vh;
}

.results {
  padding: 88px 24px 96px;
}

.results-inner {
  max-width: 1120px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

@media (min-width: 760px) {
  .results-inner {
    grid-template-columns: 1fr 1fr;
    gap: 28px;
  }
}
</style>
