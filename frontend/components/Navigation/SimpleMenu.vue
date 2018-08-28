<template lang="html">
  <div class="contact-menu">
    <div class="menu-row">
      <p>Important Stuff</p>
      <a href="#">Resume</a>
    </div>
    <div class="menu-row">
      <p>Contact</p>
      <a href="#"><i class="icon-phone"></i></a>
      <a href="#"><i class="icon-mail"></i></a>
    </div>
    <div class="menu-row">
      <p>Find me on</p>
      <a href="#">Linkedin</a>
      <a href="#">Medium</a>
    </div>
    <div class="menu-row">
      <p>Version Control</p>
      <a href="#">Github</a>
      <a href="#">Bitbucket</a>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.contact-menu {
  .menu-row {
    display: block;
    margin-left: 38px;
    margin-bottom: 10px;
    p {
      margin: 0;
      padding: 0;
      display: block;
      font-family: $gotham-rounded-medium;
      font-size: 13px;
    }
    a {
      display: inline-block;
      font-family: $proxima-nova;
      font-size: 13px;
      color: $color-gray-heavy;
      margin-right: 5px;
      text-decoration: none;
      &:hover {
        text-decoration: underline;
      }
    }
  }
}
</style>
