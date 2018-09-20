<template lang="html">
  <nav class="social-nav">
    <a href="#" v-for="(item, index) in items" :key="index">
      <i :class="display_icon(item.title)"></i>
    </a>
  </nav>
</template>

<script>
export default {
  props: ['items'],
  methods: {
    display_icon(title) {
      return `icon-${title.toLowerCase()}`
    }
  }
}
</script>

<style lang="css">
</style>
