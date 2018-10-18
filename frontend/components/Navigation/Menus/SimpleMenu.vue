<template lang="html">
  <div class="contact-menu">
    <div v-for="(item, index) in menu" :key="index" class="menu-row">
      <p>{{ item.title }}</p>
      <a
        v-for="(subItem, index2) in item.sub_menu_items"
        :key="index2"
        :style="font_size(item)"
        :href="subItem.url"
        target="_blank"
        v-html="subItem.title" />
    </div>
  </div>
</template>

<script>
export default {
  props: ['menu'],
  methods: {
    font_size(item) {
      if (item.icon == 'big-icon') {
        return 'font-size:24px;'
      } else {
        return 'font-size:13px;'
      }
    }
  }
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
      .icon-whatsapp {
        color: $color-green;
      }
      .icon-fb-messenger {
        color: #0557FF;
      }
    }
  }
}
</style>
