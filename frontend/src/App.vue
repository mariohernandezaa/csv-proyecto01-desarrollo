<script setup>
import { ref } from 'vue'
import AppHeader from './components/AppHeader.vue'
import CsvDropzone from './components/CsvDropzone.vue'
import SummaryPanel from './components/SummaryPanel.vue'
import SuggestionsPanel from './components/SuggestionsPanel.vue'

const informe = ref(null)
const resultMessage = ref('')
const errorMessage = ref('')

function handleAnalysisStart() {
  informe.value = null
  resultMessage.value = ''
  errorMessage.value = ''
}

function handleAnalysisSuccess(resultado) {
  informe.value = resultado
  resultMessage.value = `Análisis completado: ${resultado.filas} filas y ${resultado.columnas} columnas.`
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
        <SuggestionsPanel />
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
