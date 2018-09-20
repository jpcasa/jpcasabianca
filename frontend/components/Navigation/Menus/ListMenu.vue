<template lang="html">
  <ul class="list-menu">
    <li v-for="(item, index) in items" :key="index">
      {{ item.title }}
    </li>
  </ul>
</template>

<script>
export default {
  props: ['items']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

.list-menu {
  list-style: none;
  padding: 0;
  margin: 0 20px;
  font-family: $proxima-nova;
  color: #fff;
  li {
    cursor: pointer;
    margin: 3px 0;
    &:hover {
      color: $color-green-light;
    }
  }
}
</style>
