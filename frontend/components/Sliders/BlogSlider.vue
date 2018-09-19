<template lang="html">
  <section class="blog-slider">
    <div class="blog-slider-content" v-for="i in (0, 5)" :key="i">
      <img src="img/blogimg.jpeg" alt="Blog Image">
      <div class="cont80">
        <nuxt-link to="/blog/url" class="cta"><i class="icon-arrow-up-right"></i></nuxt-link>
        <p class="title">Some programs I use</p>
        <span><i class="icon-clock"></i> 6 Minute Read</span>
        <span><i class="icon-calendar"></i> September 6, 2018</span>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        <nuxt-link class="read-more" to="/blog/url">Read More</nuxt-link>
      </div>
    </div>
  </section>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.blog-slider {
  min-width: 100%;
  display: flex;
  min-height: 200px;
  overflow-x: scroll;
  .blog-slider-content {
    min-width: 320px;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
    -moz-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
    box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
    position: relative;
    margin-left: 20px;
    img {
      width: 100%;
      height: auto;
    }
    p {
      color: $color-gray-heavy;
    }
    .title {
      font-family: $gotham-rounded-medium;
      color: $color-blue-black;
      font-size: 22px;
      margin: 40px 0 10px 0;
    }
    .copy {
      font-size: 14px;
    }
    .cta {
      position: absolute;
      right: -32px;
      top: -20px;
      font-size: 22px;
      padding: 8px 10px;
      background-color: $color-green-light;
      color: $color-green-dark;
      text-decoration: none;
      z-index: 40;
      &:hover {
        background-color: $color-green;
      }
    }
    span {
      font-size: 13px;
      font-family: $gotham-rounded-medium;
      display: block;
      margin-bottom: 5px;
      color: $color-gray-heavy;
      i {
        color: $color-green;
        display: inline-block;
        margin-right: 4px;
      }
    }
    .read-more {
      color: $color-green;
      text-decoration: none;
      display: inline-block;
      margin-bottom: 25px;
      font-family: $gotham-rounded-medium;
      font-size: 15px;
      &:hover {
        text-decoration: underline;
      }
    }
  }
}

.blog-slider::-webkit-scrollbar {
  display: none;
}
.blog-slider::-webkit-scrollbar-thumb {
  display: none;
}
</style>
