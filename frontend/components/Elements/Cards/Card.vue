<template lang="html">
  <div class="card">
    <div class="card-left">
      <img src="img/program.png" alt="Program">
    </div>
    <div class="card-right">
      <span>GitHub (8.2)</span>
      <div class="progress-bar-container">
        <div class="progress-bar" />
      </div>
      <a href="#" target="_blank">Visit Website</a>
    </div>
  </div>
</template>

<script>
export default {
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
    span {
      font-size: 14px;
      font-family: $gotham-rounded-medium;
      color: $color-blue-heavy;
    }
    .progress-bar-container {
      width: 95%;
      background-color: $color-gray-light;
      height: 13px;
      margin-right: 20px;
      @include border-radius(3px);
      .progress-bar {
        width: 75%;
        height: 100%;
        @include border-radius(3px);
        background-color: $color-green-light;
      }
    }
    a {
      color: $color-gray-heavy;
      text-decoration: none;
      font-size: 14px;
      &:hover {
        color: $color-green;
        text-decoration: underline;
      }
    }
  }
}
</style>
