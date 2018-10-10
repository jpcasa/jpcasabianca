<template lang="html">
  <section class="card-slider">
    <div
      class="card-slider-content"
      v-for="(item, index) in items"
      :key="index">
      <div class="container">
        <img :src="item.place_logo" :alt="item.place">
        <p class="title">{{ item.course_title }}</p>
        <hr>
        <p class="copy">{{ item.description }}</p>
        <div class="card-slider-info">
          <span>Main Focus</span>
          <div class="" v-html="item.main_focus" />
        </div>
        <a :href="item.website" target="_blank" class="cta">
          <i class="icon-arrow-up-right"></i>
        </a>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: ['items']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.card-slider {
  min-width: 100%;
  display: flex;
  min-height: 200px;
  overflow-x: scroll;
  .card-slider-content {
    min-width: 260px;
    // display: flex;
    // flex-direction: column;
    // align-items: flex-start;
    padding: 20px 10px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
    -moz-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
    box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
    position: relative;
    margin-left: 20px;
    img {
      width: 80px;
      height: 80px;
      margin-bottom: 10px;
    }
    hr {
      border: none;
      border-bottom: 1px solid $color-gray-light;
    }
    p, ul, span {
      color: $color-gray-heavy;
    }
    .title {
      font-family: $gotham-rounded-medium;
      color: $color-blue-black;
      font-size: 14px;
      margin: 0;
    }
    .copy {
      font-size: 14px;
    }
    .cta {
      position: absolute;
      right: -25px;
      top: -20px;
      font-size: 22px;
      padding: 8px 10px;
      background-color: $color-green-light;
      color: $color-green-dark;
      text-decoration: none;
      &:hover {
        background-color: $color-green;
      }
    }
    span {
      font-size: 13px;
      font-family: $gotham-rounded-medium;
    }
    ul {
      font-size: 14px;
    }
  }
}
</style>
