<template lang="html">
  <section class="card-slider">
    <div class="card-slider-content">
      <div class="container">
        <img src="img/udemy.png" alt="Udemy">
        <p class="title">Some programs I use</p>
        <hr>
        <p class="copy">Wow, so your origin is what? You fell into a vat of redundancy?</p>
        <div class="card-slider-info">
          <span>Main Focus</span>
          <ol>
            <li>Something</li>
            <li>Something</li>
          </ol>
        </div>
        <div class="card-slider-info">
          <span>Main Focus</span>
          <ol>
            <li>Something</li>
            <li>Something</li>
          </ol>
        </div>
        <a href="#" class="cta"><i class="icon-arrow-up-right"></i></a>
      </div>
    </div>
    <div class="card-slider-content" />
    <div class="card-slider-content" />
    <div class="card-slider-content" />
    <div class="card-slider-content" />
    <div class="card-slider-content" />
  </section>
</template>

<script>
export default {
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
    display: flex;
    flex-direction: column;
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
    }
    hr {
      border: none;
      border-bottom: 1px solid $color-gray-light;
    }
    p, ol, span {
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
      right: -23px;
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
    ol {
      font-size: 14px;
    }
  }
}
</style>
