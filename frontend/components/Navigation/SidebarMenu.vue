<template lang="html">
  <ul class="sidebar-menu">
    <li v-for="(item, index) in menu" :key="index">
      <span
        :class="item.id == $store.state.menuActive ? 'active menu-item' : 'menu-item'">
        {{ item.title }}
      </span>
      <ul v-show="showSubMenu(item)">
        <li v-for="(subItem, index2) in item.sub_menu_items" :key="index2">
          <span :class="subItem.url == $store.state.subMenuActive ? 'menu-sub-item active' : 'menu-sub-item'">
            {{ subItem.title }}
          </span>
        </li>
      </ul>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['menu'],
  methods: {
    showSubMenu(item) {
      if (this.$store.state.menuActive == item.id && item.sub_menu_items.length) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.sidebar-menu {
  padding: 0;
  margin: 0 0 30px 0;
  list-style: none;
  li {
    position: relative;
    .menu-item {
      font-family: $gotham-rounded-medium;
      font-size: 14px;
      display: block;
      padding: 10px 0 10px 30px;
      border-left: 8px solid #fff;
      cursor: pointer;
      &:hover {
        background-color: $color-gray-light;
        border-left: 8px solid $color-green;
      }
    }
    .menu-item.active {
      background-color: $color-gray-light;
      border-left: 8px solid $color-green;
    }
    ul {
      list-style: none;
      margin-top: 10px;
      li {
        .menu-sub-item {
          font-family: $proxima-nova;
          display: block;
          padding: 3px 0 3px 20px;
          cursor: pointer;
          border-left: 5px solid #fff;
          color: $color-gray-heavy;
          font-size: 13px;
          &:hover {
            color: $color-blue-black;
            font-family: $proxima-nova-bold;
            border-left: 5px solid $color-green;
          }
        }
        .menu-sub-item.active {
          color: $color-blue-black;
          font-family: $proxima-nova-bold;
          border-left: 5px solid $color-green;
        }
      }
    }
  }
}
</style>
