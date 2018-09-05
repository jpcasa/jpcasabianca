<template lang="html">
  <div class="img-card">
    <img src="img/nogales.png" alt="Nogales">
    <p class="title">Colegio Los Nogales</p>
    <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod. ed diam nonummy nibh euismod.</p>
    <a class="cta" href="#">View Website</a>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.img-card {
  -webkit-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  background-color: #fff;
  @include border-radius(20px);
  display: flex;
  padding: 35px 25px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 25px;
  img {
    width: 150px;
    height: 150px;
  }
  .title {
    font-family: $gotham-rounded-medium;
    font-size: 18px;
    color: $color-blue-black;
    margin: 25px 0 15px 0;
  }
  .copy {
    color: $color-gray-heavy;
    font-size: 14px;
    margin: 0 0 15px 0;
  }
  .cta {
    text-decoration: none;
    font-size: 13px;
    font-family: $gotham-rounded-medium;
    color: $color-green;
    &:hover {
      text-decoration: underline;
    }
  }
}
</style>
