<template lang="html">
  <div class="portfolio-card">
    <span class="subtitle">{{ subtitle }}</span>
    <h1>{{ title }}</h1>
    <img class="portfolio-card-img" v-if="ctaUrl == 'printa-delivery'" src="img/printa-delivery.png" alt="Printa Delivery">
    <img class="portfolio-card-img" v-if="ctaUrl == 'mapps360'" src="img/mapps360.png" alt="Mapps360">
    <p class="copy" v-html="copy" />
    <nuxt-link v-if="!comingSoon" class="cta" :to="'/case-studies/' + ctaUrl">{{ cta }}</nuxt-link>
    <a v-if="comingSoon" class="cta">Coming Soon</a>
  </div>
</template>

<script>
export default {
  props: ['title', 'subtitle', 'copy', 'cta', 'ctaUrl', 'comingSoon'],
  created() {
    console.log(this.title)
  }
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
    cursor: pointer;
    @extend %background-green;
    @extend %cta;
  }
}
</style>
