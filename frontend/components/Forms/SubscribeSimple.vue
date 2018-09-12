<template lang="html">
  <div class="subscribe-simple">
    <input type="email" placeholder="Enter your email here..." />
    <button type="submit">Suscribe</button>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.subscribe-simple {
  display: flex;
  input {
    flex: 3;
    border: none;
    height: 40px;
    text-indent: 15px;
    font-family: $proxima-nova;
    font-size: 15px;
  }
  button {
    flex: 1;
    border: none;
    font-family: $gotham-rounded-medium;
    background-color: $color-green-light;
    font-size: 15px;
    cursor: pointer;
    &:hover {
      background-color: $color-green;
    }
  }
}
</style>
