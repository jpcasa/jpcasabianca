<template lang="html">
  <section class="horizontal-cards">
    <Card v-for="i in (0, 5)" :key="i" />
  </section>
</template>

<script>
import Card from '~/components/Elements/Cards/Card.vue'

export default {
  components: {
    Card
  }
}
</script>

<style lang="css">
</style>
