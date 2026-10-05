<script setup>
import { computed } from 'vue'

const props = defineProps({
  informe: { type: Object, default: null },
  resultMessage: { type: String, default: '' },
  errorMessage: { type: String, default: '' },
})

const filasConAusentes = computed(() =>
  (props.informe?.ausentes_por_fila ?? []).flatMap((cantidad, index) =>
    cantidad > 0 ? [{ fila: index + 1, cantidad }] : [],
  ),
)
</script>

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

    <p v-if="props.errorMessage" class="result-text upload-error" role="alert">
      {{ props.errorMessage }}
    </p>
    <template v-else-if="props.informe">
      <p class="result-text" role="status">{{ props.resultMessage }}</p>

      <dl class="summary-stats">
        <div class="summary-stat">
          <dt>Filas</dt>
          <dd>{{ props.informe.filas }}</dd>
        </div>
        <div class="summary-stat">
          <dt>Columnas</dt>
          <dd>{{ props.informe.columnas }}</dd>
        </div>
      </dl>

      <section class="detail-section">
        <h3>Tipos de datos</h3>
        <dl class="detail-list">
          <div v-for="(tipo, columna) in props.informe.tipos" :key="columna">
            <dt>{{ columna }}</dt>
            <dd>{{ tipo }}</dd>
          </div>
        </dl>
      </section>

      <section class="detail-section">
        <h3>Valores ausentes por columna</h3>
        <dl class="detail-list">
          <div v-for="(cantidad, columna) in props.informe.ausentes_por_columna" :key="columna">
            <dt>{{ columna }}</dt>
            <dd>{{ cantidad }}</dd>
          </div>
        </dl>
      </section>

      <section v-if="filasConAusentes.length" class="detail-section">
        <h3>Filas con valores ausentes</h3>
        <ul class="missing-rows">
          <li v-for="fila in filasConAusentes" :key="fila.fila">
            Fila {{ fila.fila }}: {{ fila.cantidad }} ausente(s)
          </li>
        </ul>
      </section>
    </template>
    <p v-else class="result-text" id="upload-instructions">
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

.upload-error {
  color: #ff8b8b;
}

.summary-stats {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin: 4px 0;
}

.summary-stat,
.detail-list > div {
  display: flex;
  justify-content: space-between;
  gap: 16px;
}

.summary-stat {
  padding: 12px;
  background: rgba(255, 255, 255, 0.06);
}

.summary-stat dt,
.detail-list dt {
  color: var(--muted);
}

.summary-stat dd,
.detail-list dd {
  margin: 0;
  color: var(--text-h);
  font-weight: 700;
}

.detail-section {
  display: grid;
  gap: 8px;
  margin-top: 8px;
}

.detail-section h3 {
  margin: 0;
  color: var(--text-h);
  font-size: 14px;
}

.detail-list,
.missing-rows {
  display: grid;
  gap: 6px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.detail-list > div {
  font-size: 13px;
}

.missing-rows {
  max-height: 140px;
  overflow-y: auto;
  color: var(--muted);
  font-size: 13px;
}
</style>
