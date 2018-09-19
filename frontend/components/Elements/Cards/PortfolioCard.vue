<template lang="html">
  <div class="portfolio-card">
    <span class="subtitle">Case Study #1</span>
    <h1>Ctrl + P = Problem. Solving the hazzle of printing.</h1>
    <img class="portfolio-card-img" src="img/printa-delivery.png" alt="Printa Delivery">
    <p class="copy">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
    <p class="copy">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
    <nuxt-link class="cta" to="#">Discover Printa</nuxt-link>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.portfolio-card {
  text-align: center;
  margin-bottom: 70px;
  .portfolio-card-img {
    max-width: 200px;
  }
  .copy {
    color: $color-gray-heavy;
  }
  .subtitle {
    color: $color-green;
  }
  .cta {
    @extend %background-green;
    @extend %cta;
  }
}
</style>
