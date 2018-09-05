<template lang="html">
  <div class="contact-menu">
    <div v-for="(item, index) in menu" :key="index" class="menu-row">
      <p>{{ item.title }}</p>
      <a
        v-for="(subItem, index2) in item.sub_menu_items"
        :key="index2"
        href="#"
        target="_blank"
        v-html="subItem.title" />
    </div>
  </div>
</template>

<script>
export default {
  props: ['menu']
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
