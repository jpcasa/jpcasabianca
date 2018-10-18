<template lang="html">
  <div class="mobile-contact-info-container">
    <div class="upper-info" />
    <div class="lower-info">
      <div class="container container-lower-info">
        <div class="lower-info-img">
          <img src="img/jp.png" alt="" class="profile-img-small">
        </div>
        <div class="lower-info-name">
          <p>JP Casabianca</p>
          <div class="lower-info-menu">
            <a href="mailto:hola@jpcasabianca.com" class="lower-info-menu-item">
              <i class="icon-mail"></i>
              <span class="">Email</span>
            </a>
            <a href="https://wa.me/573507015800" target="_blank" class="lower-info-menu-item">
              <i class="icon-whatsapp"></i>
              <span class="whatsapp">Whatsapp</span>
            </a>
            <a href="http://m.me/juan.p.casabianca" target="_blank" class="lower-info-menu-item">
              <i class="icon-fb-messenger"></i>
              <span class="fb">FB</span>
            </a>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="description-info">
          <div class="description-row">
            <div class="description-row-left">
              <p>Experience</p>
            </div>
            <div class="description-row-right">
              <a href="#" class="item">Resume</a>
              <span>Download Latest</span>
            </div>
          </div>
          <div class="description-row">
            <div class="description-row-left">
              <p>Important Stuff</p>
            </div>
            <div class="description-row-right">
              <div class="desc-mini">
                <a href="https://www.linkedin.com/in/juan-pablo-casabianca/" class="item"><i class="icon-linkedin-1"></i></a>
                <a href="https://medium.com/@jpc_774" class="item"><i class="icon-medium "></i></a>
                <span>Check me out</span>
              </div>
            </div>
          </div>
          <div class="description-row">
            <div class="description-row-left">
              <p>Version Control</p>
            </div>
            <div class="description-row-right">
              <a href="https://github.com/jpcasa" class="item"><i class="icon-github-logo"></i></a>
              <a href="https://bitbucket.org/jpcasabianca/" class="item"><i class="icon-atlassian "></i></a>
              <span>Latest Work</span>
            </div>
          </div>
          <div class="description-row">
            <div class="description-row-left">
              <p>Portfolio</p>
            </div>
            <div class="description-row-right">
              <a href="https://dribbble.com/jpcasabianca" class="item"><i class="icon-dribbble-big-logo"></i></a>
              <a href="https://www.behance.net/holae2af" class="item"><i class="icon-behance-logo"></i></a>
              <span>Don't be shy</span>
            </div>
          </div>
          <div class="description-row">
            <div class="description-row-left" />
            <div class="description-row-right">
              <a href="tel:573507015800" id="call">Call</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['menu']
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.mobile-contact-info-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  .upper-info {
    background-image: url('/img/mobile.png');
    background-size: cover;
    flex: 4;
  }
  .lower-info {
    flex: 5;
    .container {
      width: 80%;
    }
    .container-lower-info {
      display: flex;
      flex-direction: row;
      margin-bottom: -30px;
      .lower-info-img {
        flex: 1;
        .profile-img-small {
          width: 130px;
          height: 130px;
          position: relative;
          bottom: 65px;
          @include border-radius(50%);
          -webkit-box-shadow: 0px 0px 9px -2px rgba(0,0,0,0.56);
          -moz-box-shadow: 0px 0px 9px -2px rgba(0,0,0,0.56);
          box-shadow: 0px 0px 9px -2px rgba(0,0,0,0.56);
        }
      }
      .lower-info-name {
        flex: 1;
        font-family: $gotham-rounded-medium;
        p {
          margin-bottom: 10px;
          margin-left: 14px;
        }
        .lower-info-menu {
          display: flex;
          .lower-info-menu-item {
            flex: 1;
            text-align: center;
            text-decoration: none;
            i, span {
              display: block;
              color: $color-gray-heavy;
            }
            span {
              margin-top: 4px;
              font-size: 12px;
              font-family: $proxima-nova;
            }
            .icon-whatsapp,
            .whatsapp {
              color: $color-green;
            }
            .icon-fb-messenger,
            .fb {
              color: $color-blue;
            }
          }
        }
      }
    }
    .description-row {
      display: flex;
      font-family: $proxima-nova;
      margin-bottom: 10px;
      p {
        font-size: 14px;
      }
      span {
        font-size: 12px;
      }
      .description-row-left {
        flex: 4;
        p {
          margin: 0;
          color: $color-gray-heavy;
        }
      }
      .description-row-right {
        flex: 5;
        p {
          margin: 0;
          color: $color-blue-heavy;
          i {
            display: inline-block;
            margin-right: 8px;
            cursor: pointer;
          }
        }
        span {
          color: $color-gray-heavy;
          display: block;
        }
        .item {
          padding: 0;
          margin: 0 5px 0 0;
          background: none;
          display: inline-block;
          color: #1a2a40;
          &:hover {
            background: none;
            text-decoration: underline;
          }
        }
      }
    }
  }
}

#call {
  text-decoration: none;
  display: inline-block;
  padding: 9px 45px;
  font-family: $gotham-rounded-medium;
  font-size: 14px;
  @include border-radius($border-radius);
  @extend %background-green;
  margin-top: 10px;
}
</style>
