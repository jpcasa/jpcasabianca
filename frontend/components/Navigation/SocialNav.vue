<template lang="html">
  <nav class="social-nav">
    <a v-for="(item, index) in items"
      :key="index"
      :href="item.url"
      target="_blank">
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
