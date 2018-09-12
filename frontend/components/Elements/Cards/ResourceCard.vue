<template lang="html">
  <div class="resource-card text-center">
    <div class="container">
      <img class="resource-img" src="img/resource1.png" alt="Resource">
      <p class="resource-title">Stay up to date</p>
      <p class="resource-copy">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
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

.resource-card {
  background-color: #fff;
  @include border-radius($border-radius);
  display: inline-block;
  padding: 10px 0;
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
  .resource-copy {
    color: $color-gray-heavy;
    font-size: 15px;
    font-family: $proxima-nova;
  }
}
</style>
