<template lang="html">
  <section class="horizontal-cards">
    <Card v-for="(item, index) in items" :key="index" :card="item" />
  </section>
</template>

<script>
import Card from '~/components/Elements/Cards/Card.vue'

export default {
  props: ['items'],
  components: {
    Card
  }
}
</script>

<style lang="css">
</style>
