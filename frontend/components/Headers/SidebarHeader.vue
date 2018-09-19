<template lang="html">
  <header id="desktop-sidebar" class="desktop">
    <!-- LOGO -->
    <nuxt-link class="main-logo" to="/">
      <img src="img/logo2.png" alt="Logo JP Casabianca">
    </nuxt-link>
    <!-- SIDEBAR HEADER -->
    <SidebarMenu id="sidebar-header" :menu="menu" />
    <!-- SIMPLE MENU -->
    <SimpleMenu :menu="contact" />
  </header>
</template>

<script>
import SidebarMenu from '~/components/Navigation/Menus/SidebarMenu.vue'
import SimpleMenu from '~/components/Navigation/Menus/SimpleMenu.vue'

export default {
  props: ['menu', 'contact'],
  components: {
    SidebarMenu,
    SimpleMenu
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

#desktop-sidebar {
  z-index: 200;
  width: $sidebar-width;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #fff;
  border-right: 1px solid $color-gray-light;
  overflow-y: scroll;
  .main-logo {
    display: block;
    font-size: 20px;
    text-decoration: none;
    color: $color-blue-heavy;
    font-family: $gotham-rounded-medium;
    margin: 20px 0 20px 30px;
    &:hover {
      color: $color-green;
    }
    img {
      width: 140px;
      height: auto;
    }
  }
}
</style>
