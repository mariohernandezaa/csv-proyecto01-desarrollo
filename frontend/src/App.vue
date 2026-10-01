<script setup>
import AppHeader from './components/AppHeader.vue'
import CsvDropzone from './components/CsvDropzone.vue'
import SummaryPanel from './components/SummaryPanel.vue'
import SuggestionsPanel from './components/SuggestionsPanel.vue'
</script>

<template>
  <div class="app">
    <AppHeader />
    <CsvDropzone />
    <section class="results">
      <div class="results-inner">
        <SummaryPanel />
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
