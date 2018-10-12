<template lang="html">
  <div class="skill-card">

    <!-- SKILL CARD CONTENT -->
    <div class="skill-card-content" @click="showDetail(skill)">
      <i v-if="skill.preferred" class="favorite icon-star"></i>
      <span class="skill-level">{{ skill.skill_level }}</span>
      <img class="skill-logo" :src="skill.logo" alt="Vuejs" />
      <span class="skill-title">{{ skill.name }}</span>
    </div>

  </div>
</template>

<script>
import RadarChart from '~/components/Elements/Charts/RadarChart.js'

export default {
  props: ['skill'],
  data() {
    return {
      showSkillDetail: false,
      chartData: {
        labels: ['Running', 'Swimming', 'Eating', 'Cycling', 'Eating', 'Cycling'],
        datasets: [{
          data: [9, 10, 6, 7, 8, 9],
          backgroundColor: 'rgba(62, 236, 130, 0.5)',
          borderColor: '#23c286',
        }]
      }
    }
  },
  components: {
    RadarChart
  },
  methods: {
    showDetail(skill) {
      this.$emit('clicked', skill)
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';
@import '~/assets/css/helpers/_extensions.scss';

.chartjs-render-monitor {
  max-width: 300px;
  margin: auto;
}

.skill-card {
  width: 140px;
  background-color: #fff;
  margin: 10px;
  text-align: center;
  padding-top: 30px;
  position: relative;
  .skill-card-content {
    cursor: pointer;
    .skill-logo {
      width: 80px;
      height: 80px;
      margin: auto;
    }
    .skill-title {
      display: block;
      cursor: pointer;
      font-family: $gotham-rounded-medium;
      color: $color-blue-black;
      font-size: 14px;
      padding: 12px 0;
      &:hover {
        color: $color-green-dark;
        background-color: $color-green-light;
      }
    }
    .favorite {
      position: absolute;
      left: 8px;
      top: 8px;
      color: $color-green;
    }
    .skill-level {
      position: absolute;
      top: 10px;
      right: 8px;
      font-size: 13px;
      font-family: $gotham-rounded-medium;
    }
  }
  .skill-detail {
    position: fixed;
    right: 0;
    top: 0;
    width: 100%;
    max-width: 450px;
    height: 100%;
    z-index: 1000;
    background-color: #fff;
    overflow-y: scroll;
    .top {
      background-color: $color-green-light;
      padding: 25px 0;
      position: fixed;
      width: 100%;
      max-width: 450px;
      top: 0;
      right: 0;
      z-index: 1100;
      i {
        display: inline-block;
        font-size: 36px;
        color: $color-green-dark;
        cursor: pointer;
        @include border-radius(50%);
        &:hover {
          background-color: $color-green;
        }
      }
      .icon-x-circle {
        float: left;
      }
      .img-circle {
        position: absolute;
        left: 37%;
        width: 80px;
        height: 80px;
        bottom: -50px;
        padding: 15px;
        @include border-radius(50%);
        background-color: #fff;
        -webkit-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
        -moz-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
        box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
        overflow: hidden;
        img {
          width: 100%;
          height: 100%;
          margin: auto;
        }
      }
    }
    .skill-content {
      .skill-name {
        margin-top: 155px;
        font-family: $gotham-rounded-medium;
        color: $color-blue-black;
      }
      .skill-info {
        text-align: left;
        margin-bottom: 25px;
        .skill-info-copy {
          color: $color-gray-heavy;
          font-family: $proxima-nova;
          font-size: 14px;
          margin: 0;
        }
        a.skill-info-copy {
          &:hover {
            color: $color-green;
          }
        }
        .skill-info-title {
          font-family: $gotham-rounded-medium;
          font-size: 15px;
          margin: 0 0 5px 0;
        }
        .dot-chart-row {
          flex: 6;
          display: flex;
          .circle-container {
            flex: 1;
            text-align: left;
            .circle {
              display: inline-block;
              width: 18px;
              height: 18px;
              background-color: $color-gray;
              margin-right: 5px;
              @include border-radius(50%);
            }
            .circle.active {
              background-color: $color-green-light;
            }
          }
        }
      }
    }
  }
}

@media (min-width: 768px) {
  #radar-chart {
    // margin-left: 0;
    // margin-right: 0;
  }
}
</style>
