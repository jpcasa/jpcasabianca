<template lang="html">
  <ul id="navigation-mobile">
    <li
      v-for="(item, index) in menu"
      :class="item.id == $store.state.subMenuActive ? 'active' : ''"
      :key="index">
      <i :class="'icon-' + item.icon"></i>
      <span>{{ item.title }}</span>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['menu']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

#navigation-mobile {
  display: flex;
  position: fixed;
  z-index: 190;
  width: 100%;
  bottom: 0;
  left: 0;
  background-color: $color-blue-black;
  text-align: center;
  padding: 0;
  margin: 0;
  list-style: none;
  li {
    flex: 1;
    color: $color-gray;
    padding: 0;
    margin: 0;
    padding: 5px 0;
    cursor: pointer;
    i,
    span {
      display: block;
    }
    i {
      margin-bottom: 6px;
    }
    span {
      font-size: 10px;
      font-family: $gotham-rounded-book;
    }
    &:hover {
      background-color: $color-green-light;
      color: $color-green-dark;
    }
  }
  .active {
    background-color: $color-green-light;
    color: $color-green-dark;
  }
}

@media (min-width: 600px) {
  #navigation-mobile {
    li {
      span {
        font-size: 13px;
      }
      i {
        font-size: 18px;
      }
    }
  }
}

@media (min-width: 992px) {
  #navigation-mobile {
    display: none;
  }
}
</style>
