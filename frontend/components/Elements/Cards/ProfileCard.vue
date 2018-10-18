<template lang="html">
  <div class="profile-card">
    <div class="profile-card-top">
      <div class="profile-card-top-left">
        <div class="img-circle">
          <img :src="testimony.avatar" alt="algo">
        </div>
      </div>
      <div class="profile-card-top-right">
        <a :href="testimony.linkedin" target="_blank" class="name">{{ testimony.person }}</a>
        <p class="job">{{ testimony.job }}</p>
      </div>
    </div>
    <div class="profile-card-bottom">
      <p>{{ testimony.testimony }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['testimony']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

.profile-card {
  display: flex;
  flex-direction: column;
  background-color: #fff;
  -webkit-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  box-shadow: 0px 0px 18px -1px rgba(0,0,0,0.2);
  position: relative;
  padding: 15px 20px;
  text-align: left;
  margin-bottom: 25px;
  @include border-radius($border-radius);
  .profile-card-top {
    display: flex;
    align-items: center;
    .profile-card-top-left {
      flex: 1;
      .img-circle {
        width: 40px;
        height: 40px;
        @include border-radius(50%);
        overflow: hidden;
        img {
          height: 100%;
          width: 100%;
        }
      }
    }
    .profile-card-top-right {
      flex: 4;
      p, a {
        margin: 0;
      }
      .name {
        font-family: $gotham-rounded-medium;
        color: $color-blue-black;
        font-size: 15px;
        text-decoration: none;
        &:hover {
          text-decoration: underline;
        }
      }
      .job {
        font-size: 14px;
        color: $color-green;
      }
    }
  }
  .profile-card-bottom {
    margin-top: 10px;
    p {
      font-size: 14px;
      color: $color-gray-heavy;
      margin: 0;
    }
  }
}

@media (min-width: 768px) {
  .profile-card {
    .profile-card-top {
      .profile-card-top-left {
        flex: 1;
      }
      .profile-card-top-right {
        flex: 7;
      }
    }
  }
}
</style>
