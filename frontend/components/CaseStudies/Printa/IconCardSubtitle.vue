<template lang="html">
  <div class="printa-icon-card">
    <img v-if="info.icon == 'p0'" src="~/static/img/printa/p0.png" alt="Icon ALT">
    <img v-if="info.icon == 'p1'" src="~/static/img/printa/p1.png" alt="Icon ALT">
    <img v-if="info.icon == 'p2'" src="~/static/img/printa/p2.png" alt="Icon ALT">
    <h3 class="title">{{ info.title }}</h3>
    <p class="subtitle helvetica-light-italic">{{ info.subtitle }}</p>
    <p class="copy">{{ info.copy }}</p>
  </div>
</template>

<script>
export default {
  props: ['info']
}
</script>

<style lang="scss">
.printa-icon-card {
  margin-bottom: 70px;
  display: block;
  img {
    width: 160px;
    margin-bottom: 15px;
  }
  .title {
    margin: 0 0 5px 0;
  }
  .subtitle {
    margin: 0 0 30px 0;
  }
}
</style>
