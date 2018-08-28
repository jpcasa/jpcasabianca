<template lang="html">
  <div class="subscribe">
    <p>A Short Timeline</p>
    <h2>Suscribe to my Newsletter</h2>
    <form class="" action="index.html" method="post">
      <input type="email" name="email" placeholder="Email">
      <input type="submit" value="Suscribe">
    </form>
  </div>
</template>

<script>
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.subscribe {
  text-align: center;
  display: block;
  max-width: 600px;
  margin: auto;
  p {
    color: $color-green-light;
    margin: 0;
  }
  h2 {
    margin: 10px 0 15px 0;
    color: #fff;
  }
  form {
    display: flex;
    input[type="email"],
    input[type="submit"] {
      height: 40px;
      border: none;
      @include border-radius($border-radius);
    }
    input[type="email"] {
      flex: 5;
      margin-right: 20px;
      background-color: $color-blue-black;
      text-indent: 15px;
    }
    input[type="email"]::placeholder {
      color: $color-gray;
      font-family: $proxima-nova;
    }
    input[type="submit"] {
      flex: 1;
      background-color: $color-green-light;
      color: $color-green-dark;
      font-family: $gotham-rounded-medium;
    }
  }
}
</style>
