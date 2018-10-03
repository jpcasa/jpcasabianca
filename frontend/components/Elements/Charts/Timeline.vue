<template lang="html">
  <section class="timeline-container">
    <div class="timeline" v-if="items">
      <div class="timeline-content">
        <div class="item">
          <article class="">
            <span class="subtitle">{{ items[0].start_date }} - {{ items[0].end_date }}</span>
            <p class="title">{{ items[0].job_title }}</p>
            <p class="company">@{{ items[0].company }} - {{ items[0].place }}</p>
            <p class="copy">{{ items[0].summary }}</p>
          </article>
          <div class="arrow" />
          <div class="circle" />
        </div>
      </div>
      <div class="timeline-content" />
      <div class="timeline-content">
        <div class="item">
          <article class="">
            <span class="subtitle">{{ items[2].start_date }} - {{ items[2].end_date }}</span>
            <p class="title">{{ items[2].job_title }}</p>
            <p class="company">@{{ items[2].company }} - {{ items[2].place }}</p>
            <p class="copy">{{ items[2].summary }}</p>
          </article>
          <div class="arrow" />
          <div class="circle" />
        </div>
      </div>
      <div class="timeline-content" />
      <div class="timeline-content">
        <div class="item">
          <article class="">
            <span class="subtitle">{{ items[4].start_date }} - {{ items[4].end_date }}</span>
            <p class="title">{{ items[4].job_title }}</p>
            <p class="company">@{{ items[4].company }} - {{ items[4].place }}</p>
            <p class="copy">{{ items[4].summary }}</p>
          </article>
          <div class="arrow" />
          <div class="circle" />
        </div>
      </div>
      <div class="timeline-content" />
      <div class="timeline-content" />
    </div>
    <div class="timeline-divider">
      <div class="timeline-divider-line" />
    </div>
    <div class="timeline">
      <div class="timeline-content" />
      <div class="timeline-content">
        <div class="item">
          <div class="arrow-up" />
          <div class="circle-up" />
          <article class="">
            <span class="subtitle">{{ items[1].start_date }} - {{ items[1].end_date }}</span>
            <p class="title">{{ items[1].job_title }}</p>
            <p class="company">@{{ items[1].company }} - {{ items[1].place }}</p>
            <p class="copy">{{ items[1].summary }}</p>
          </article>
        </div>
      </div>
      <div class="timeline-content" />
      <div class="timeline-content">
        <div class="item">
          <div class="arrow-up" />
          <div class="circle-up" />
          <article class="">
            <span class="subtitle">{{ items[3].start_date }} - {{ items[3].end_date }}</span>
            <p class="title">{{ items[3].job_title }}</p>
            <p class="company">@{{ items[3].company }} - {{ items[3].place }}</p>
            <p class="copy">{{ items[3].summary }}</p>
          </article>
        </div>
      </div>
      <div class="timeline-content" />
      <div class="timeline-content">
        <div class="item">
          <div class="arrow-up" />
          <div class="circle-up" />
          <article class="">
            <span class="subtitle">{{ items[5].start_date }} - {{ items[5].end_date }}</span>
            <p class="title">{{ items[5].job_title }}</p>
            <p class="company">@{{ items[5].company }} - {{ items[5].place }}</p>
            <p class="copy">{{ items[5].summary }}</p>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: ['items']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.timeline-container {
  min-width: 100%;
  display: flex;
  flex-direction: column;
  overflow: -moz-scrollbars-none;
  overflow-x: scroll;
  text-align: center;
  .timeline-divider {
    width: 2000px;
    height: 30px;
    align-items: center;
    display: flex;
    margin: 50px 0;
    .timeline-divider-line {
      width: 100%;
      margin-left: 185px;
      border-bottom: 3px solid #85949e;
    }
  }
  .timeline {
    min-width: 100%;
    min-height: 180px;
    display: flex;
    .timeline-content {
      min-width: 300px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: 0 30px;
      .item {
        background-color: #fff;
        width: 90%;
        margin: auto;
        height: 200px;
        padding: 12px 25px;
        flex: 5;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        @include border-radius($border-radius);
        .arrow,
        .arrow-up {
          position: absolute;
          height: 65px;
          width: 4px;
          left: 160px;
          background-color: $color-green-light;
        }
        .arrow {
          bottom: -65px;
        }
        .arrow-up {
          top: -65px;
        }
        .circle,
        .circle-up {
          position: absolute;
          height: 20px;
          width: 20px;
          left: 152px;
          @include border-radius(50%);
          background-color: $color-green-light;
        }
        .circle {
          bottom: -75px;
        }
        .circle-up {
          top: -75px;
        }
        article {
          .subtitle {
            color: $color-green;
            font-size: 13px;
          }
          .title {
            margin: 5px 0;
            font-family: $gotham-rounded-medium;
            color: $color-blue-black;
          }
          .copy {
            color: $color-gray-heavy;
            font-size: 14px;
            margin: 0;
          }
          .company {
            color: $color-gray-heavy;
            font-size: 13px;
            margin: 0 0 10px 0;
            // font-family: $gotham-rounded-book;
          }
        }
      }
      .line {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        .timeline-line {
          display: block;
          height: 2px;
          background-color: #000;
          width: 100%;
        }
      }
      .space {
        flex: 5;
      }
    }
  }
  .timeline::-webkit-scrollbar {
    display: none;
  }
}

.timeline-container::-webkit-scrollbar {
  display: none;
}
.timeline-container::-webkit-scrollbar-thumb {
  display: none;
}
</style>
