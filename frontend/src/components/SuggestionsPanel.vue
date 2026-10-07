<script setup></script>

<template>
  <article class="panel">
    <header class="panel-header">
      <span class="panel-tag">Sugerencias</span>
      <h2 class="panel-title">Sugerencias orientativas</h2>
      <p class="panel-subtitle">Preguntas de análisis y criterios para valores ausentes</p>
    </header>

    <div class="panel-body">
      <p class="panel-text">
        Cuando se cargue un archivo, aquí aparecerán preguntas de análisis sugeridas
        y recomendaciones para tratar los valores ausentes.
      </p>
    </div>
  </article>
</template>

<style scoped>
.panel {
  background: var(--surface);
  border: 1px solid var(--border-hover);
  box-shadow: var(--shadow-card);
  overflow: hidden;
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
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.02em;
  color: var(--text-h);
}

.panel-subtitle {
  font-size: 15px;
  color: var(--text-main);
}

.panel-body {
  padding: 28px 32px 32px;
}

.panel-text {
  font-size: 15px;
  line-height: 1.6;
  color: var(--text-main);
}

@media (max-width: 520px) {
  .panel-header,
  .panel-body {
    padding-left: 20px;
    padding-right: 20px;
  }
}
</style>
