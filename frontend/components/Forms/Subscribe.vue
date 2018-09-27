<template lang="html">
  <div class="subscribe">
    <p>I hate spam just as much as you...</p>
    <h2>Subscribe to my newsletter</h2>
    <span>I read a lot of stuff every week and love to stay up to date with everything happening. Sometimes it’s overwhelming, so I usually pin out the most important news of the week with a newsletter.</span>
    <form class="" action="index.html" method="post">
      <input type="email" name="email" placeholder="Enter your email...">
      <input type="submit" value="Subscribe">
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
    margin: 10px 0;
    color: #fff;
  }
  span {
    color: $color-gray;
    font-size: 14px;
    display: block;
    margin-bottom: 20px;
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
      color: $color-gray;
      font-family: $proxima-nova;
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
      cursor: pointer;
      &:hover {
        background-color: $color-green;
      }
    }
  }
}
</style>
