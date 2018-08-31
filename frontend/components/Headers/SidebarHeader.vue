<template lang="html">
  <header id="desktop-sidebar" class="desktop">
    <!-- LOGO -->
    <nuxt-link class="main-logo" to="/">JP Casabianca</nuxt-link>
    <!-- SIDEBAR HEADER -->
    <SidebarMenu id="sidebar-header" :menu="menu" />
    <!-- SIMPLE MENU -->
    <SimpleMenu :menu="contact" />
  </header>
</template>

<script>
import SidebarMenu from '~/components/Navigation/SidebarMenu.vue'
import SimpleMenu from '~/components/Navigation/SimpleMenu.vue'

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
  .main-logo {
    display: block;
    font-size: 20px;
    text-decoration: none;
    color: $color-blue-heavy;
    font-family: $gotham-rounded-medium;
    margin: 30px 0 30px 30px;
    &:hover {
      color: $color-green;
    }
  }
}
</style>
