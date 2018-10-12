<template lang="html">
  <div class="card">
    <div class="card-left">
      <img :src="card.logo" :alt="card.name">
    </div>
    <div class="card-right">
      <a :href="card.website" target="_blank">{{ card.name }}</a>
      <p>{{ card.summary }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['card'],
  methods: {
    progress(skill_level) {
      const level = (skill_level / 10) * 100
      return `width: ${level}%;`
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.card {
  text-align: left;
  display: flex;
  align-items: center;
  padding: 10px 0;
  width: 100%;
  -webkit-box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
  -moz-box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
  box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
  margin-bottom: 15px;
  .card-left {
    flex: 1;
    text-align: center;
    img {
      width: 50px;
      height: 50px;
    }
  }
  .card-right {
    flex: 4;
    a {
      font-size: 14px;
      font-family: $gotham-rounded-medium;
      color: $color-blue-heavy;
      text-decoration: none;
      &:hover {
        color: $color-green;
      }
    }
    p {
      color: $color-gray-heavy;
      font-size: 14px;
      margin: 0;
    }
  }
}
</style>
