<template lang="html">
  <div class="title-with-cta">
    <p class="subtitle">{{ subtitle }}</p>
    <h2 class="title">{{ title }}</h2>
    <p class="copy" v-html="copy" />
    <nuxt-link
      class="cta"
      v-show="action == 'push'"
      :to="ctaUrl">
      {{ cta }}
    </nuxt-link>
    <button
      class="cta"
      v-show="action == 'scroll'">
      {{ cta }}
    </button>
  </div>
</template>

<script>
import DynamicTitle from '~/components/Elements/Titles/DynamicTitle.vue'

export default {
  props: ['title', 'subtitle', 'copy', 'cta', 'ctaUrl', 'action'],
  components: {
    DynamicTitle
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.title-with-cta {
  display: block;
  max-width: 500px;
  margin: auto;
  .subtitle {
    color: $color-green-light;
    margin-bottom: 5px;
  }
  .title {
    font-family: $gotham-rounded-medium;
    color: #fff;
    margin: 0;
  }
  .copy {
    color: $color-gray;
  }
  .cta {
    @extend %cta;
  }
}
</style>
