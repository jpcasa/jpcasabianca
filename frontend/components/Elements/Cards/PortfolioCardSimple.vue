<template lang="html">
  <div class="portfolio-card-simple">
    <nuxt-link v-if="!comingSoon" to="" class="portfolio-cta"><span class="icon-arrow-up-right"></span></nuxt-link>
    <img class="portfolio-card-img" :src="'img/' + url + '.png'" :alt="title">
    <div class="tags" v-html="tags" />
    <nuxt-link v-if="!comingSoon" :to="'/case-studies/' + url" class="cta">View More</nuxt-link>
  </div>
</template>

<script>
export default {
  props: ['url', 'title', 'tags', 'comingSoon']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.portfolio-card-simple {
  text-align: center;
  background-color: #fff;
  position: relative;
  width: 250px;
  padding: 20px 0;
  margin: 50px 0;
  -webkit-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  .portfolio-cta {
    position: absolute;
    right: 0;
    top: 0;
    text-decoration: none;
    background-color: $color-green-light;
    color: $color-green-dark;
    padding: 5px 6px;
    &:hover {
      background-color: $color-green;
    }
    span {
      font-size: 22px;
    }
  }
  .portfolio-card-img {
    max-width: 200px;
    margin-bottom: 20px;
  }
  .tags {
    display: flex;
    margin: 0 20px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 15px;
    span {
      display: inline-block;
      padding: 4px 8px;
      background-color: $color-green-light;
      font-size: 13px;
      margin: 0 3px 5px 3px;
      color: $color-green-dark;
      font-family: $gotham-rounded-medium;
    }
  }
  .cta {
    text-decoration: none;
    color: $color-green;
    font-size: 13px;
    font-family: $gotham-rounded-medium;
    &:hover {
      text-decoration: underline;
    }
  }
}
</style>
