<script setup>
</script>

<template>
  <header class="hero">
    <div class="topbar">
      <span class="brand">CPP<span class="brand-dot">.</span></span>
      <p class="brand-lede">Por Mario y Alex!</p>
    </div>

    <div class="hero-inner">
      <div class="hero-content">
        <h1 class="title">
          CSV <span class="accent-word">Preanálisis</span> de Pruebas
        </h1>
        <p class="lede">Explora y entiende tus datos antes de analizarlos.</p>
      </div>

      <div class="hero-media">
        <div class="hero-glow" aria-hidden="true"></div>
        <img src="/img/heropng.png" alt="" class="hero-img" />
      </div>
    </div>
  </header>
</template>

<style scoped>
.hero {
  width: 100%;
  background: linear-gradient(160deg, var(--hero-bg-start) 0%, var(--hero-bg-end) 100%);
  padding-bottom: 80px;
  overflow: hidden;
}

.topbar {
  max-width: 1120px;
  margin: 0 auto;
  padding: 28px 24px 0;
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

.hero-inner {
  max-width: 1120px;
  margin: 0 auto;
  padding: 44px 24px 0;
  display: grid;
  grid-template-columns: 1fr;
  align-items: center;
  gap: 24px;
}

.hero-content {
  display: flex;
  flex-direction: column;
  gap: 18px;
  position: relative;
  z-index: 2;
}

.title {
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.14;
  letter-spacing: -0.01em;
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
  position: relative;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  min-height: 260px;
}

.hero-glow {
  position: absolute;
  width: 50vw;
  height: 50vh;
  border-radius: 50%;
  bottom: 0;
}

.hero-img {
  position: relative;
  width: 100%;
  max-width: 300px;
  height: auto;
  filter: drop-shadow(0 24px 24px rgba(22, 20, 20, 0.18));
}

@media (min-width: 860px) {
  .hero-inner {
    grid-template-columns: 1.1fr 0.9fr;
    gap: 40px;
    padding-top: 60px;
  }

  .title {
    font-size: 3.4rem;
  }

  .hero-media {
    min-height: 400px;
  }

  .hero-glow {
    width: 340px;
    height: 340px;
  }

  .hero-img {
    max-width: 380px;
  }
}
</style>
