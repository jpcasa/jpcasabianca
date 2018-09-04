<template lang="html">
  <div class="filter-dropdown">
    <span>Filter Programs</span>
    <p @click="toggle()"><i :class="icon"></i> Business &amp; Finance</p>
    <transition name="fadeHeight">
      <ul v-show="showDropdown" class="filter-dropdown-container">
        <li class="active">item</li>
        <li>item</li>
        <li>item</li>
        <li>item</li>
        <li>item</li>
        <li>item</li>
      </ul>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDropdown: false,
      icon: 'icon-arrow-down'
    }
  },
  methods: {
    toggle() {
      this.showDropdown = !this.showDropdown
      if (this.showDropdown) {
        this.icon = 'icon-arrow-up'
      } else {
        this.icon = 'icon-arrow-down'
      }
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.filter-dropdown {
  text-align: center;
  span {
    display: block;
    color: $color-green;
    font-size: 13px;
    margin-bottom: 5px;
  }
  p {
    display: block;
    position: relative;
    background-color: $color-gray-light;
    margin-top: 5px;
    padding: 10px 0;
    font-family: $gotham-rounded-medium;
    color: $color-blue-black;
    font-size: 15px;
    cursor: pointer;
    @include border-radius($border-radius);
    @include transition(all 0.3s);
    &:hover {
      background-color: $color-green-light;
      color: $color-green-dark;
      i {
        color: $color-green-dark;
      }
    }
    i {
      position: absolute;
      left: 15px;
      top: 9px;
      font-size: 20px;
      color: $color-green;
      @include transition(all 0.3s);
    }
  }
  .filter-dropdown-container {
    list-style: none;
    padding: 0;
    margin: 0;
    font-family: $gotham-rounded-medium;
    font-size: 15px;
    margin-bottom: 20px;
    border: 1px solid $color-gray-light;
    @include border-radius($border-radius);
    li {
      color: $color-gray-heavy;
      padding: 10px 0;
      cursor: pointer;
      border-bottom: 1px solid $color-gray-light;
      &:hover {
        background-color: $color-gray-light;
        color: $color-blue-black;
      }
      &:first-child {
        @include single-border-radius($border-radius, top, left);
        @include single-border-radius($border-radius, top, right);
      }
      &:last-child {
        @include single-border-radius($border-radius, bottom, left);
        @include single-border-radius($border-radius, bottom, right);
      }
    }
    .active {
      background-color: $color-green-light;
      color: $color-green-dark;
    }
  }
}

.fadeHeight-enter-active,
.fadeHeight-leave-active {
  transition: all 0.4s;
  max-height: 230px;
}
.fadeHeight-enter,
.fadeHeight-leave-to
{
  opacity: 0;
  max-height: 0px;
}
</style>
