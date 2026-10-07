<script setup>
const props = defineProps({
  suggestions: { type: Object, default: null },
  loading: { type: Boolean, default: false },
  errorMessage: { type: String, default: '' },
  canGenerate: { type: Boolean, default: false },
})

const emit = defineEmits(['generate-suggestions'])
</script>

<template>
  <article class="panel suggestions-panel">
    <header class="panel-header">
      <span class="panel-tag">Sugerencias</span>
      <h2 class="panel-title">Sugerencias orientativas</h2>
      <p class="panel-subtitle">Preguntas de análisis y criterios para valores ausentes</p>
    </header>

    <div class="panel-body">
      <p v-if="!props.canGenerate" class="panel-text">
        Carga un archivo CSV para generar preguntas de análisis y recomendaciones para tratar los valores ausentes.
      </p>

      <p v-if="props.loading" class="panel-status" role="status">
        Generando preguntas de análisis y recomendaciones...
      </p>

      <p v-else-if="props.errorMessage" class="panel-text upload-error" role="alert">
        {{ props.errorMessage }}
      </p>

      <template v-else-if="props.suggestions">
        <section class="suggestion-section">
          <h3>Preguntas de análisis</h3>
          <ul>
            <li v-for="pregunta in props.suggestions.preguntas_analisis" :key="pregunta">
              {{ pregunta }}
            </li>
          </ul>
        </section>

        <section class="suggestion-section">
          <h3>Tratamientos de valores ausentes</h3>
          <div
            v-for="tratamiento in props.suggestions.tratamientos"
            :key="tratamiento.columna"
            class="treatment"
          >
            <strong>{{ tratamiento.columna }}</strong>
            <ul>
              <li v-for="opcion in tratamiento.opciones" :key="opcion">
                {{ opcion }}
              </li>
            </ul>
          </div>
        </section>

        <p class="panel-text disclaimer">{{ props.suggestions.aviso }}</p>
      </template>

      <button
        v-if="props.canGenerate && !props.suggestions"
        class="generate-button"
        type="button"
        :disabled="props.loading"
        @click="emit('generate-suggestions')"
      >
        {{ props.loading ? 'Generando sugerencias…' : 'Generar sugerencias' }}
      </button>
    </div>
  </article>
</template>

<style scoped>
.panel {
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--border-hover);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card);
}

.panel-header {
  display: grid;
  gap: 6px;
  padding: 28px 32px 24px;
  background: color-mix(in srgb, var(--text-h) 3%, transparent);
  border-bottom: 1px solid var(--border);
}

.panel-tag {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent-text);
}

.panel-title {
  margin-top: 4px;
  font-size: 2rem;
  line-height: 1.15;
  color: var(--text-h);
}

.panel-subtitle {
  font-size: 15px;
  color: var(--text-main);
}

.panel-body {
  display: grid;
  gap: 22px;
  padding: 28px 32px 32px;
}

.panel-text {
  font-size: 15px;
  line-height: 1.6;
  color: var(--text-main);
}

.panel-status {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  border: 1px solid var(--accent-border);
  border-radius: var(--radius-md);
  background: var(--accent-bg);
  color: var(--accent-text);
}

.panel-status::before {
  content: '';
  width: 8px;
  height: 8px;
  flex: 0 0 auto;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 5px var(--accent-bg);
  animation: pulse 1.4s ease-in-out infinite;
}

.upload-error {
  padding: 12px 14px;
  border: 1px solid color-mix(in srgb, var(--danger) 28%, transparent);
  border-radius: var(--radius-md);
  background: color-mix(in srgb, var(--danger) 8%, transparent);
  color: var(--danger);
}

.suggestion-section {
  display: grid;
  gap: 9px;
}

.suggestion-section h3 {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 3px 0 1px;
  color: var(--text-h);
  font-size: 14px;
}

.suggestion-section h3::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
}

.suggestion-section ul,
.treatment ul {
  margin: 0;
  padding-left: 20px;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.6;
}

.treatment {
  display: grid;
  gap: 5px;
  padding: 12px 14px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

.treatment strong {
  color: var(--text-h);
  font-size: 13px;
}

.generate-button {
  width: 100%;
  margin-top: 4px;
  padding: 14px 20px;
  border: 1px solid var(--accent);
  border-radius: var(--radius-md);
  background: var(--accent);
  color: var(--accent-on);
  font: inherit;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 10px 24px -12px var(--accent-text);
  transition: transform 0.2s var(--ease), background-color 0.2s var(--ease), box-shadow 0.2s var(--ease);
}

.generate-button:hover:not(:disabled) {
  background: var(--accent-text);
  border-color: var(--accent-text);
  transform: translateY(-1px);
  box-shadow: 0 14px 28px -14px var(--accent-text);
}

.generate-button:active:not(:disabled) {
  transform: translateY(0) scale(0.99);
}

.generate-button:focus-visible {
  outline: 3px solid var(--accent-bg);
  outline-offset: 3px;
}

.generate-button:disabled {
  cursor: wait;
  opacity: 0.72;
}

.disclaimer {
  padding-top: 10px;
  border-top: 1px solid var(--border);
  font-size: 12.5px;
}

@keyframes pulse {
  0%, 100% { opacity: 0.45; transform: scale(0.88); }
  50% { opacity: 1; transform: scale(1); }
}

@media (max-width: 640px) {
  .panel-header,
  .panel-body {
    padding-left: 20px;
    padding-right: 20px;
  }

  .panel-title {
    font-size: 1.65rem;
  }
}
</style>
