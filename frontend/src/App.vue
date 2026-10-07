<script setup>
import { ref, nextTick } from 'vue'
import AppHeader from './components/AppHeader.vue'
import CsvDropzone from './components/CsvDropzone.vue'
import SummaryPanel from './components/SummaryPanel.vue'
import SuggestionsPanel from './components/SuggestionsPanel.vue'

const vista = ref('inicio')
const informe = ref(null)
const resultMessage = ref('')
const errorMessage = ref('')

const reducirMovimiento = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

// La tarjeta se expande hasta ocupar la vista (y se contrae al volver) con View Transitions;
// donde no exista, o si el usuario pide menos movimiento, el cambio es directo.
function abrirVista(nombre) {
  window.scrollTo(0, 0)

  const cambiar = () => {
    vista.value = nombre
    return nextTick()
  }

  if (document.startViewTransition && !reducirMovimiento) {
    document.startViewTransition(cambiar)
  } else {
    cambiar()
  }
}

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
    <nav class="nav">
      <div class="nav-brand">
        <span class="brand">CPP<span class="brand-dot">.</span></span>
        <span class="brand-lede">Por Mario y Alex!</span>
      </div>
      <button
        v-if="vista !== 'inicio'"
        type="button"
        class="nav-back"
        @click="abrirVista('inicio')"
      >
        ← Volver al inicio
      </button>
    </nav>

    <main v-if="vista === 'inicio'" class="home">
      <div class="home-grid">
        <AppHeader />

        <div class="service-stack">
          <button type="button" class="service service--accent" @click="abrirVista('preanalisis')">
            <span class="service-kicker">Preanálisis</span>
            <span class="service-title">Revisa tu CSV</span>
            <span class="service-text">Filas, columnas, tipos de datos y valores ausentes en un solo informe.</span>
            <span class="service-go" aria-hidden="true">→</span>
          </button>

          <button type="button" class="service service--ink" @click="abrirVista('ia')">
            <span class="service-kicker">Sugerencias IA</span>
            <span class="service-title">Ideas para investigar</span>
            <span class="service-text">Preguntas de análisis y criterios orientativos para tratar los valores ausentes.</span>
            <span class="service-go" aria-hidden="true">→</span>
          </button>
        </div>
      </div>
    </main>

    <main v-else-if="vista === 'preanalisis'" class="detail detail--preanalisis">
      <CsvDropzone
        @analysis-start="handleAnalysisStart"
        @analysis-success="handleAnalysisSuccess"
        @analysis-error="handleAnalysisError"
      />
      <SummaryPanel
        :informe="informe"
        :result-message="resultMessage"
        :error-message="errorMessage"
      />
    </main>

    <main v-else class="detail detail--ia">
      <SuggestionsPanel />
    </main>
  </div>
</template>

<style scoped>
.app {
  width: 100%;
  min-height: 100vh;
}

.nav {
  max-width: 1440px;
  margin: 0 auto;
  padding: 20px 32px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.nav-brand {
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.brand {
  font-family: var(--font-display);
  font-size: 22px;
  letter-spacing: 0.02em;
  color: var(--text-h);
}

.brand-dot {
  color: var(--accent);
}

.brand-lede {
  font-size: 13px;
  color: var(--muted);
}

.nav-back {
  padding: 9px 18px;
  border: 1px solid var(--border-hover);
  border-radius: 999px;
  background: var(--surface);
  color: var(--text-h);
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: border-color 0.2s var(--ease);
}

.nav-back:hover {
  border-color: var(--text-h);
}

.home {
  max-width: 1440px;
  margin: 0 auto;
  padding: 24px 32px 96px;
}

.home-grid {
  display: grid;
  gap: 20px;
}

.service-stack {
  display: grid;
  gap: 20px;
}

.service {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
  min-height: 210px;
  padding: 28px 32px;
  border: none;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-edge);
  font: inherit;
  text-align: left;
  cursor: pointer;
  transition: transform 0.2s var(--ease), box-shadow 0.2s var(--ease);
}

.service:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 0 1px var(--border-hover), 0 32px 56px -24px rgba(15, 23, 42, 0.45);
}

.service:active {
  transform: scale(0.99);
}

.service--accent {
  background: var(--accent);
  color: var(--accent-on);
  view-transition-name: card-preanalisis;
}

.service--ink {
  background: var(--text-h);
  color: var(--bg-app);
  view-transition-name: card-ia;
}

.home .service {
  animation: rise 0.6s var(--ease) backwards;
}

.home .service:nth-child(2) {
  animation-delay: 0.1s;
}

@keyframes rise {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
}

.service-kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  opacity: 0.8;
}

.service-title {
  font-size: 1.75rem;
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.02em;
}

.service-text {
  font-size: 15px;
  line-height: 1.5;
  opacity: 0.85;
  max-width: 36ch;
}

.service-go {
  margin-top: auto;
  align-self: flex-end;
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border: 1.5px solid currentColor;
  border-radius: 50%;
  font-size: 18px;
}

.detail {
  max-width: 1440px;
  margin: 0 auto;
  padding: 24px 32px 96px;
  display: grid;
  gap: 24px;
  animation: fade-in 0.4s var(--ease) backwards;
}

.detail--preanalisis {
  view-transition-name: card-preanalisis;
}

.detail--ia {
  view-transition-name: card-ia;
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
}

@media (max-width: 640px) {
  .nav,
  .home,
  .detail {
    padding-left: 16px;
    padding-right: 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .home .service,
  .detail {
    animation: none;
  }
}

@media (min-width: 860px) {
  .home-grid {
    grid-template-columns: 1.35fr 1fr;
    align-items: stretch;
  }

  .service-stack {
    grid-template-rows: 1fr 1fr;
  }
}
</style>
