<template lang="html">
  <div class="skill-detail">
    <div class="top">
      <div class="container clearfix">
        <i class="icon-x-circle" @click="closeDetail()" />
      </div>
      <div class="img-circle">
        <img :src="skill.logo" alt="">
      </div>
    </div>
    <div class="skill-content">
      <div class="container">
        <p class="skill-name">{{ skill.name }}</p>
        <div class="skill-info">
          <p class="skill-info-title">Skill Level</p>
          <div class="dot-chart-row">
            <div v-for="j in (0, 10)" :key="j" class="circle-container">
              <span :class="j <= skill.skill_level ? 'circle active' : 'circle'" />
            </div>
          </div>
        </div>
        <div class="skill-info">
          <p class="skill-info-title">Worked</p>
          <span class="skill-info-copy">{{ skill.months_worked }} Months</span>
        </div>
        <div class="skill-info">
          <p class="skill-info-title">Last Project with {{ skill.name }}</p>
          <a :href="skill.last_project" class="skill-info-copy">{{ skill.last_project }}</a>
        </div>
        <!-- <div class="skill-info">
          <p class="skill-info-title">Last Project with Vue.js</p>
          <RadarChart
            :data="chartData" />
        </div> -->
        <div class="skill-info">
          <p class="skill-info-title">Website</p>
          <a :href="skill.website" class="skill-info-copy">{{ skill.website }}</a>
        </div>
        <div class="skill-info">
          <p class="skill-info-title">Documentation</p>
          <a :href="skill.documentation" class="skill-info-copy">{{ skill.documentation }}</a>
        </div>
        <div class="skill-info">
          <p class="skill-info-title">Github</p>
          <a :href="skill.github" class="skill-info-copy">{{ skill.github }}</a>
        </div>
        <div class="skill-info">
          <p class="skill-info-title">Why I use {{ skill.name }}?</p>
          <span class="skill-info-copy">{{ skill.why }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RadarChart from '~/components/Elements/Charts/RadarChart.js'

export default {
  props: ['skill'],
  data() {
    return {
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
    closeDetail() {
      this.$emit('clicked')
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';
@import '~/assets/css/helpers/_extensions.scss';

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
        color: #000;
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
    padding-bottom: 40px;
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
</style>
