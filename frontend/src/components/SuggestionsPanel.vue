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
  <article class="result-card surface-card">
    <div class="icon-badge result-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9.09 9a3 3 0 1 1 5.82 1c0 2-3 3-3 3" />
        <line x1="12" y1="17" x2="12.01" y2="17" />
        <circle cx="12" cy="12" r="10" />
      </svg>
    </div>
    <p class="eyebrow">Sugerencias</p>
    <h2 class="result-title">Sugerencias orientativas</h2>

    <p v-if="props.loading" class="result-text" role="status">
      Generando preguntas de análisis y recomendaciones...
    </p>

    <p v-else-if="props.errorMessage" class="result-text upload-error" role="alert">
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

      <p class="result-text disclaimer">{{ props.suggestions.aviso }}</p>
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

    <p v-else-if="!props.canGenerate" class="result-text">
      Cuando se cargue un archivo, aquí aparecerán preguntas de análisis sugeridas
      y recomendaciones para tratar los valores ausentes.
    </p>
  </article>
</template>

<style scoped>
.result-card {
  position: relative;
  overflow: hidden;
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  border-color: var(--border-hover);
  background:
    linear-gradient(145deg, var(--surface) 0%, var(--bg-subtle) 100%);
}

.result-card::after {
  content: '';
  position: absolute;
  width: 160px;
  height: 160px;
  right: -74px;
  top: -82px;
  border-radius: 50%;
  background: var(--accent-bg);
  pointer-events: none;
}

.result-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 2px;
  background: var(--accent-bg);
  border-color: var(--accent-border);
  color: var(--accent-text);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.08);
}

.result-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-h);
}

.result-text {
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--muted);
}

.result-text[role='status'] {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  border: 1px solid var(--accent-border);
  border-radius: var(--radius-md);
  background: var(--accent-bg);
  color: var(--accent-text);
}

.result-text[role='status']::before {
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
  border: 1px solid rgba(255, 113, 113, 0.34);
  border-radius: var(--radius-md);
  background: rgba(255, 113, 113, 0.08);
  color: #c63c3c;
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
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.01em;
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
  .result-card {
    padding: 26px 22px;
  }

  .result-icon {
    width: 44px;
    height: 44px;
  }
}
</style>
