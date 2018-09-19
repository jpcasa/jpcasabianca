<template lang="html">
  <div class="inbound-cards">
    <div class="inbound-card">
      <div class="inbound-card-left">
        <img src="img/awareness.svg" alt="">
      </div>
      <div class="inbound-card-right">
        <p class="title">Awareness</p>
        <span class="subtitle">Global Trainee - Bavaria</span>
        <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet.</p>
      </div>
    </div>
    <div class="inbound-card">
      <div class="inbound-card-left">
        <img src="img/interest.svg" alt="">
      </div>
      <div class="inbound-card-right">
        <p class="title">Interest</p>
        <span class="subtitle">Global Trainee - Bavaria</span>
        <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet.</p>
      </div>
    </div>
    <div class="inbound-card">
      <div class="inbound-card-left">
        <img src="img/desire.svg" alt="">
      </div>
      <div class="inbound-card-right">
        <p class="title">Desire</p>
        <span class="subtitle">Global Trainee - Bavaria</span>
        <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet.</p>
      </div>
    </div>
    <div class="inbound-card">
      <div class="inbound-card-left">
        <img src="img/action.svg" alt="">
      </div>
      <div class="inbound-card-right">
        <p class="title">Action</p>
        <span class="subtitle">Global Trainee - Bavaria</span>
        <p class="copy">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

.inbound-cards {
  .inbound-card {
    display: flex;
    align-items: center;
    -webkit-box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
    -moz-box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
    box-shadow: 0px 0px 18px -1px rgba(223,227,234,1);
    padding: 15px 10px;
    margin-bottom: 20px;
    .inbound-card-left {
      flex: 1;
      margin-right: 15px;
      img {
        width: 70px;
      }
    }
    .inbound-card-right {
      flex: 3;
      p {
        margin: 0;
      }
      .title {
        font-family: $gotham-rounded-medium;
        font-size: 14px;
        color: $color-blue-black;
      }
      .subtitle {
        color: $color-green;
        font-size: 14px;
        display: block;
        margin-bottom: 8px;
      }
      .copy {
        font-size: 14px;
        color: $color-gray-heavy;
      }
    }
  }
}

@media (min-width: 768px) {
  .inbound-cards {
    .inbound-card {
      .inbound-card-left {
        flex: 1;
      }
      .inbound-card-right {
        flex: 5;
      }
    }
  }
}
</style>
