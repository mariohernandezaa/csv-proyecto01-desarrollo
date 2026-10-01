<script setup></script>

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
    <p class="result-text">
      Cuando se cargue un archivo, aquí aparecerán preguntas de análisis sugeridas
      y recomendaciones para tratar los valores ausentes.
    </p>
  </article>
</template>

<style scoped>
.result-card {
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.result-icon {
  width: 44px;
  height: 44px;
  margin-bottom: 6px;
}

.result-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-h);
}

.result-text {
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--muted);
}
</style>
