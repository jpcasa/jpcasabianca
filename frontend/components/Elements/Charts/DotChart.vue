<template lang="html">
  <div class="dot-chart">
    <div v-for="(item, index) in items" :key="index" class="dot-chart-row">
      <div class="dot-chart-row-left">
        <span>{{ item.name }}</span>
      </div>
      <div class="dot-chart-row-right">
        <div v-for="j in (0, 10)" :key="j" class="circle-container">
          <span :class="j <= item.skill_level ? 'circle active' : 'circle'" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['items']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.dot-chart {
  display: flex;
  flex-direction: column;
  justify-content: center;
  .dot-chart-row {
    display: flex;
    margin-bottom: 12px;
    .dot-chart-row-left {
      flex: 1;
      margin-right: 15px;
      span {
        color: #fff;
      }
    }
    .dot-chart-row-right {
      flex: 6;
      display: flex;
      .circle-container {
        flex: 1;
        text-align: center;
        .circle {
          display: inline-block;
          width: 15px;
          height: 15px;
          background-color: $color-blue-black;
          margin: 0 5px;
          @include border-radius(50%);
        }
        .circle.active {
          background-color: $color-green-light;
        }
      }
    }
  }
}
</style>
