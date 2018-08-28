<template lang="html">
  <footer id="main-footer">
    <div class="container">
      <Subscribe />
      <div class="footer-menus">
        <ListMenu />
        <ListMenu />
        <ListMenu />
      </div>
    </div>
  </footer>
</template>

<script>
import Subscribe from '~/components/Forms/Subscribe.vue'
import ListMenu from '~/components/Navigation/ListMenu.vue'

export default {
  components: {
    Subscribe,
    ListMenu
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

#main-footer {
  display: block;
  background-color: $color-blue-heavy;
}

.footer-menus {
  justify-content: center;
  display: flex;
}
</style>
