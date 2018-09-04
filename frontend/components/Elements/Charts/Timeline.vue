<template lang="html">
  <section class="timeline-container">
    <div class="timeline">
      <div class="timeline-content">
        <div class="item">
          <article class="">
            <span class="subtitle">A Short Timeline</span>
            <p class="title">Experience &amp; Work</p>
            <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh.</p>
          </article>
          <div class="arrow" />
          <div class="circle" />
        </div>
      </div>
      <div class="timeline-content" />
      <div class="timeline-content">
        <div class="item">
          <article class="">
            <span class="subtitle">A Short Timeline</span>
            <p class="title">Experience &amp; Work</p>
            <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh.</p>
          </article>
          <div class="arrow" />
          <div class="circle" />
        </div>
      </div>
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
            <span class="subtitle">A Short Timeline</span>
            <p class="title">Experience &amp; Work</p>
            <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh.</p>
          </article>
        </div>
      </div>
      <div class="timeline-content" />
      <div class="timeline-content">
        <div class="item">
          <div class="arrow-up" />
          <div class="circle-up" />
          <article class="">
            <span class="subtitle">A Short Timeline</span>
            <p class="title">Experience &amp; Work</p>
            <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh.</p>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.timeline-container {
  min-width: 100%;
  display: flex;
  flex-direction: column;
  overflow-x: scroll;
  text-align: center;
  .timeline-divider {
    width: 880px;
    height: 30px;
    align-items: center;
    display: flex;
    margin: 50px 0;
    .timeline-divider-line {
      width: 100%;
      margin-left: 118px;
      border-bottom: 3px solid #85949e;
    }
  }
  .timeline {
    min-width: 100%;
    min-height: 180px;
    display: flex;
    .timeline-content {
      min-width: 250px;
      display: flex;
      flex-direction: column;
      .item {
        background-color: #fff;
        width: 90%;
        margin: auto;
        height: 200px;
        padding: 12px 0;
        flex: 5;
        display: flex;
        align-items: center;
        position: relative;
        @include border-radius($border-radius);
        .arrow,
        .arrow-up {
          position: absolute;
          height: 65px;
          width: 4px;
          left: 110px;
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
          left: 102px;
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
            margin: 5px 0 10px 0;
            font-family: $gotham-rounded-medium;
            color: $color-blue-black;
          }
          .copy {
            color: $color-gray-heavy;
            font-size: 14px;
            margin: 0;
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
</style>
