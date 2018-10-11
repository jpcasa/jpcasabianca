<template lang="html">
  <div class="printa-icon-card">
    <img v-if="info.icon == 'icon1'" src="~/static/img/printa/icon-1.png" alt="Icon ALT">
    <img v-if="info.icon == 'icon2'" src="~/static/img/printa/icon-2.png" alt="Icon ALT">
    <img v-if="info.icon == 'icon3'" src="~/static/img/printa/icon-3.png" alt="Icon ALT">
    <img v-if="info.icon == 'test1'" src="~/static/img/printa/test1.png" alt="Icon ALT">
    <img v-if="info.icon == 'test2'" src="~/static/img/printa/test2.png" alt="Icon ALT">
    <img v-if="info.icon == 'test3'" src="~/static/img/printa/test3.png" alt="Icon ALT">
    <h3 v-html="info.title" />
    <p>{{ info.copy }}</p>
  </div>
</template>

<script>
export default {
  props: ['info']
}
</script>

<style lang="scss">
.printa-icon-card {
  margin-bottom: 50px;
  display: block;
  img {
    width: 160px;
  }
  h3 {
    margin: 25px 0;
  }
}
</style>
