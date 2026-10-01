<script setup></script>

<template>
  <article class="result-card surface-card">
    <div class="icon-badge result-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v16a2 2 0 0 0 2 2h16" />
        <path d="M7 16l4-6 4 4 5-8" />
      </svg>
    </div>
    <p class="eyebrow">Informe</p>
    <h2 class="result-title">Informe básico</h2>
    <p class="result-text">
      Sube un archivo CSV para ver aquí filas, columnas, tipos de datos y valores ausentes.
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
