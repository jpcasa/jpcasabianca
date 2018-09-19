<template lang="html">
  <div class="tabs-full-simple">
    <nav class="resource-options">
      <a
        v-for="(item, index) in items"
        :key="index"
        v-html="item.title"
        @click="active = item.id"
        :style="anchor_style"
        :class="active == item.id ? 'active' : ''" />
    </nav>
    <div class="content text-center">
      <p :style="copy_style" v-html="copy" />
    </div>
  </div>
</template>

<script>
export default {
  props: ['styles', 'items'],
  data() {
    return {
      active: 0
    }
  },
  computed: {
    copy() {
      return this.items[this.active].copy
    },
    anchor_style() {
      if (this.styles == 'light') {
        return 'color: #0c1623'
      } else {
        return 'color: #fff'
      }
    },
    copy_style() {
      if (this.styles == 'light') {
        return 'color: #85949e'
      } else {
        return 'color: #adc7db'
      }
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

.tabs-full-simple {
  .resource-options {
    display: flex;
    width: 100%;
    text-align: center;
    margin-bottom: 30px;
    a {
      flex: 1;
      text-decoration: none;
      font-family: $gotham-rounded-medium;
      color: $color-blue-black;
      border-bottom: 1px solid $color-gray;
      padding-bottom: 15px;
      font-size: 13px;
      cursor: pointer;
      &:hover {
        border-bottom: 3px solid $color-green;
      }
    }
    a.active {
      border-bottom: 3px solid $color-green;
    }
  }
  .content {
    color: $color-gray-heavy;
    p {
      font-size: 15px;
    }
  }
}
</style>
