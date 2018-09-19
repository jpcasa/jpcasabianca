<template lang="html">
  <div class="tabs-full-simple">
    <nav class="resource-options">
      <a
        v-for="(item, index) in items"
        :key="index"
        v-html="item.title"
        @click="active = item.id"
        :class="active == item.id ? 'active' : ''" />
    </nav>
    <div class="content text-center">
      <div class="card" v-for="(card, index) in this.items[active].cards" :key="index">
        <img :src="card.icon" alt="">
        <a href="#" target="_blank" class="title">{{ card.title }}</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['items'],
  data() {
    return {
      active: 0
    }
  },
  computed: {
    copy() {
      return this.items[this.active].copy
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

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
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    .card {
      width: 150px;
      background-color: #fff;
      margin-right: 10px;
      margin-bottom: 15px;
      -webkit-box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
      -moz-box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
      box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
      padding: 20px 0;
      display: inline-block;
      text-align: center;
      @include border-radius($border-radius);
      img {
        width: 60px;
        height: auto;
        margin-bottom: 10px;
      }
      .title {
        margin: 0;
        padding: 0;
        display: block;
        font-family: $gotham-rounded-medium;
        font-size: 13px;
        text-decoration: none;
        color: $color-green;
      }
    }
  }
}
</style>
