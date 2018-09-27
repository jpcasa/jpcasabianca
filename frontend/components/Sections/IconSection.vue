<template lang="html">
  <section class="icon-section">
    <IconContent v-for="(item, index) in items" :key="index" :item="item" />
  </section>
</template>

<script>
import IconContent from '~/components/Elements/Content/IconContent.vue'

export default {
  props: ['items'],
  components: {
    IconContent
  }
}
</script>

<style lang="scss">
.icon-section {
  display: flex;
  flex-direction: column;
  .icon-content {
    flex: 1;
    margin-bottom: 40px;
  }
}
</style>
