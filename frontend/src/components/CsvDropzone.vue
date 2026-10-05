<script setup>
import { ref } from 'vue'

const emit = defineEmits(['analysis-start', 'analysis-success', 'analysis-error'])
const fileInput = ref(null)
const isLoading = ref(false)

function openFilePicker() {
  fileInput.value?.click()
}

async function handleFileChange(event) {
  const archivo = event.target.files?.[0]
  if (!archivo) return

  isLoading.value = true
  emit('analysis-start')

  try {
    const formData = new FormData()
    formData.append('file', archivo)

    const response = await fetch('/api/analyze', {
      method: 'POST',
      body: formData,
    })
    const informe = await response.json()

    if (!response.ok) {
      throw new Error(informe.detail || 'No se pudo analizar el archivo')
    }

    emit('analysis-success', informe)
    
  } catch (error) {
    emit('analysis-error', error instanceof Error ? error.message : 'No se pudo analizar el archivo')
  } finally {
    isLoading.value = false
    event.target.value = ''
  }
}
</script>

<template>
  <section class="widget-wrap">
    <div class="widget">
      <div class="icon-badge widget-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
          <polyline points="17 8 12 3 7 8"/>
          <line x1="12" y1="3" x2="12" y2="15"/>
        </svg>
      </div>

      <div class="widget-text">
        <p class="widget-title">Arrastra tu CSV aquí</p>
        <p class="widget-hint">o selecciona un archivo desde tu equipo</p>
      </div>

      <input
        ref="fileInput"
        class="file-input"
        type="file"
        accept=".csv,text/csv"
        @change="handleFileChange"
      />
      <button type="button" class="btn widget-button" :disabled="isLoading" @click="openFilePicker">
        {{ isLoading ? 'Analizando...' : 'Elegir archivo' }}
      </button>
      
    </div>
  </section>
</template>

<style scoped>
.widget-wrap {
  max-width: 1120px;
  margin: -64px auto 0;
  padding: 0 24px;
  position: relative;
  z-index: 5;
}

.widget {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 18px;
  padding: 64px 40px;
  border-radius: 0;
  border: 1.5px dashed var(--accent-border);
  background: rgba(41, 41, 41, 0.494);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
  box-shadow: var(--shadow-lift);
  cursor: pointer;
  transition: border-color 0.2s var(--ease), background-color 0.2s var(--ease);
}

.widget:hover {
  background: rgba(51, 50, 50, 0.85);
}

.widget-icon {
  width: 60px;
  height: 60px;
  border-radius: 0;
}

.widget-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.widget-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-h);
}

.widget-hint {
  font-size: 14px;
  color: var(--muted);
}

.widget-button {
  margin-top: 10px;
  border-radius: 999px;
  background: var(--accent);
  color: #ffffff;
  padding: 14px 34px;
  font-size: 14px;
  font-weight: 700;
}

.widget-button:hover {
  background: var(--accent-text);
}

.file-input {
  display: none;
}

.upload-message {
  margin: 0;
  color: var(--text-h);
  font-size: 14px;
}

.upload-error {
  color: #ff8b8b;
}

@media (max-width: 640px) {
  .widget-wrap {
    margin-top: -44px;
  }

  .widget {
    padding: 48px 24px;
  }
}
</style>
