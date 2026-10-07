<script setup>
</script>

<template>
  <header class="hero">
    <div class="hero-content">
      <h1 class="title">
        CSV <span class="accent-word">Preanálisis</span> de Pruebas
      </h1>
      <p class="lede">Explora y entiende tus datos antes de analizarlos.</p>
    </div>

    <div class="hero-media">
      <img src="/img/heropng.png" alt="" class="hero-img" />
    </div>
  </header>
</template>

<style scoped>
.hero {
  width: 100%;
  background: linear-gradient(160deg, var(--hero-bg-start) 0%, var(--hero-bg-end) 100%);
  display: flex;
  flex-direction: column;
  gap: 40px;
  height: 100%;
  padding: 44px 40px 0;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-edge);
  animation: hero-in 0.7s var(--ease) backwards;
}

@keyframes hero-in {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .hero {
    animation: none;
  }
}

.hero-content {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.title {
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.14;
  color: var(--text-h);
}

.accent-word {
  font-family: var(--font-display);
  font-weight: 400;
  color: var(--accent);
}

.lede {
  font-size: 16px;
  color: var(--text-main);
  max-width: 38ch;
  line-height: 1.6;
}

.hero-media {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  margin-top: auto;
}

.hero-img {
  width: 100%;
  max-width: 320px;
  height: auto;
  filter: drop-shadow(0 24px 24px rgba(15, 23, 42, 0.16));
}

@media (min-width: 860px) {
  .title {
    font-size: 3.4rem;
  }

  .hero {
    padding: 56px 48px 0;
  }

  .hero-img {
    max-width: 380px;
  }
}

@media (max-width: 520px) {
  .hero {
    padding: 32px 24px 0;
  }

  .title {
    font-size: 2rem;
  }
}
</style>
