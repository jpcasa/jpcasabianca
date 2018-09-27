<template lang="html">
  <div class="resource-card text-center">
    <nuxt-link to="/resources/url" class="resource-card-cta"><i class="icon-arrow-up-right"></i></nuxt-link>
    <div class="container">
      <img class="resource-img" src="img/resource1.png" alt="Resource">
      <p class="resource-title">{{ resource.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['resource']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.resource-card {
  background-color: #fff;
  display: inline-block;
  padding: 30px 0;
  margin-bottom: 30px;
  position: relative;
  -webkit-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  .resource-img {
    width: 80px;
    height: 80px;
    margin: auto;
  }
  .resource-title {
    font-family: $gotham-rounded-medium;
    font-size: 18px;
    color: $color-blue-black;
  }
  .resource-card-cta {
    position: absolute;
    right: 0;
    top: 0;
    text-decoration: none;
    background-color: $color-green-light;
    color: $color-green-dark;
    display: inline-block;
    padding: 8px;
    z-index: 30;
    cursor: pointer;
    &:hover {
      background-color: $color-green;
    }
    i {
      font-size: 20px;
    }
  }
}
</style>
