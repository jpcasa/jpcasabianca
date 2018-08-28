<template lang="html">
  <ul class="list-menu">
    <li>About Me</li>
    <li>Creative Process</li>
    <li>My Tech Stack</li>
    <li>Case Studies</li>
    <li>Resources</li>
    <li>Blog</li>
  </ul>
</template>

<script>
export default {
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
    &:hover {
      color: $color-green-light;
    }
  }
}
</style>
