<template lang="html">
  <nav class="tabs-full">
    <a v-for="(item, index) in items" :key="index">{{ item.name }}</a>
  </nav>
</template>

<script>
export default {
  props: ['items']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.tabs-full {
  display: flex;
  width: 100%;
  @include border-radius($border-radius);
  background-color: $color-blue-black;
  a {
    flex: 1;
    color: #fff;
    font-size: 14px;
    cursor: pointer;
    padding: 8px 0;
    @include border-radius($border-radius-small);
    &:hover {
      background-color: $color-green-light;
      color: $color-green-dark;
    }
  }
}
</style>
