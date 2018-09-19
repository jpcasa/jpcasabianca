<template lang="html">
  <div class="icon-content text-center">
    <img class="icon-content-img" :src="item.icon" :alt="item.title">
    <p class="title">{{ item.title }}</p>
    <span class="subtitle">{{ item.subtitle }}</span>
    <p class="copy">{{ item.copy }}</p>
  </div>
</template>

<script>
export default {
  props: ['item']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

.icon-content {
  .icon-content-img {
    width: 80px;
    height: auto;
  }
  .title {
    color: $color-blue-black;
    font-family: $gotham-rounded-medium;
    font-size: 15px;
    margin: 20px 0 5px 0;
  }
  .subtitle {
    font-size: 14px;
    color: $color-green;
    font-family: $proxima-nova;
  }
  .copy {
    color: $color-gray-heavy;
    font-family: $proxima-nova;
    font-size: 14px;
  }
}
</style>
