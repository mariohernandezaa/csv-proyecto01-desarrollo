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
  <article class="panel summary-panel">
    <header class="panel-header">
      <span class="panel-tag">Informe</span>
      <h2 class="panel-title">Informe básico</h2>
      <p class="panel-subtitle">Resumen estructural del archivo cargado</p>
    </header>

    <div class="panel-body">
      <p v-if="props.errorMessage" class="panel-text upload-error" role="alert">
        {{ props.errorMessage }}
      </p>
      <template v-else-if="props.informe">
        <p class="panel-status" role="status">{{ props.resultMessage }}</p>

        <dl class="kpis">
          <div class="kpi">
            <dt>Filas</dt>
            <dd>{{ props.informe.filas }}</dd>
          </div>
          <div class="kpi">
            <dt>Columnas</dt>
            <dd>{{ props.informe.columnas }}</dd>
          </div>
        </dl>

        <div class="detail-grid">
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
            <ul class="detail-list detail-list--scroll">
              <li v-for="fila in filasConAusentes" :key="fila.fila">
                <span>Fila {{ fila.fila }}</span>
                <span>{{ fila.cantidad }} ausente(s)</span>
              </li>
            </ul>
          </section>
        </div>
      </template>
      <p v-else class="panel-text" id="upload-instructions">
        Sube un archivo CSV para ver aquí filas, columnas, tipos de datos y valores ausentes.
      </p>
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
  gap: 28px;
  padding: 28px 32px 32px;
}

.panel-status {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-h);
}

.panel-text {
  font-size: 15px;
  line-height: 1.6;
  color: var(--text-main);
}

.upload-error {
  color: var(--danger);
  font-weight: 600;
}

.kpis {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin: 0;
}

.kpi {
  padding: 22px 24px;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  background: color-mix(in srgb, var(--text-h) 4%, transparent);
}

.kpi dt {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-main);
}

.kpi dd {
  margin: 6px 0 0;
  font-size: 2.75rem;
  line-height: 1;
  color: var(--text-h);
  font-variant-numeric: tabular-nums;
}

.detail-grid {
  display: grid;
  gap: 28px;
}

.detail-section {
  display: grid;
  gap: 10px;
  align-content: start;
}

.detail-section h3 {
  margin: 0;
  font-size: 15px;
  font-weight: 700;
  color: var(--text-h);
}

.detail-list {
  display: grid;
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: 15px;
  border-top: 1px solid var(--border-hover);
}

.detail-list > div,
.detail-list > li {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
}

.detail-list dt {
  min-width: 0;
  overflow-wrap: anywhere;
  color: var(--text-main);
}

.detail-list dd {
  flex-shrink: 0;
  margin: 0;
  font-weight: 600;
  color: var(--text-h);
  font-variant-numeric: tabular-nums;
}

.detail-list li span:last-child {
  flex-shrink: 0;
  font-weight: 600;
  color: var(--text-h);
  font-variant-numeric: tabular-nums;
}

.detail-list--scroll {
  max-height: 220px;
  overflow-y: auto;
}

@media (min-width: 760px) {
  .detail-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 520px) {
  .panel-header,
  .panel-body {
    padding-left: 20px;
    padding-right: 20px;
  }

  .panel-title {
    font-size: 1.65rem;
  }

  .kpi dd {
    font-size: 2.25rem;
  }
}
</style>
