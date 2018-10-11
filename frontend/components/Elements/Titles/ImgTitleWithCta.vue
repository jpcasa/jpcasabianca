<template lang="html">
  <div :class="'title-with-cta ' + className">
    <p class="subtitle">{{ subtitle }}</p>
    <h2 class="title">{{ title }}</h2>
    <img src="img/jp.png" alt="">
    <p class="copy" v-html="copy" />
    <nuxt-link
      class="cta"
      v-show="action == 'push'"
      :to="ctaUrl">
      {{ cta }}
    </nuxt-link>
    <button
      class="cta"
      v-scroll-to="'#' + ctaUrl"
      v-show="action == 'scroll'">
      {{ cta }}
    </button>
  </div>
</template>

<script>
import DynamicTitle from '~/components/Elements/Titles/DynamicTitle.vue'

export default {
  props: ['title', 'subtitle', 'img', 'copy', 'cta', 'ctaUrl', 'action', 'className'],
  components: {
    DynamicTitle
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.title-with-cta {
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
  img {
    margin-top: 20px;
    width: 170px;
    height: 170px;
  }
  .copy {
    color: $color-gray-heavy;
    a {
      color: $color-green;
    }
  }
  .cta {
    @extend %cta;
  }
}
.title-with-cta.dark {
  .subtitle {
    color: $color-green;
    margin-bottom: 5px;
  }
  .title {
    font-family: $gotham-rounded-medium;
    margin: 0;
    color: $color-blue-heavy;
  }
  .copy {
    color: $color-gray-heavy;
  }
  .cta {
    @extend %cta;
  }
}
</style>
