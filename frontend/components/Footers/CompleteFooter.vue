<template lang="html">
  <footer id="main-footer">
    <div class="container">
      <Subscribe />
      <div class="footer-menus">
        <ListMenu :items="footer1" />
        <ListMenu :items="footer2" />
      </div>
      <div class="footer-info">
        <p>Bogotá, Colombia.</p>
        <a class="footer-info-cta" href="mailto:hola@jpcasabianca.com">hola@jpcasabianca.com</a>
        <a class="footer-info-cta" href="tel:+573507015800">+(57) 350 701 5800</a>
        <SocialNav :items="socialMenu" />
      </div>
    </div>
    <div class="lower-footer">
      <p>&copy;2018 Copyrights. All rights reserved. <br> Made with <i class="icon-heart"></i> by <span>JP Casabianca</span>.</p>
    </div>
  </footer>
</template>

<script>
import Subscribe from '~/components/Forms/Subscribe.vue'
import ListMenu from '~/components/Navigation/Menus/ListMenu.vue'
import SocialNav from '~/components/Navigation/SocialNav.vue'

export default {
  components: {
    Subscribe,
    ListMenu,
    SocialNav
  },
  computed: {
    footer1() {
      return this.$store.state.menus.footer1.menu_items
    },
    footer2() {
      return this.$store.state.menus.footer2.menu_items
    },
    socialMenu() {
      return this.$store.state.menus.socialMenu.menu_items
    }
  },
  created() {
    this.$store.dispatch('menus/getFooterMenus')
    this.$store.dispatch('menus/getSocialMenu')
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';
@import '~/assets/css/helpers/_extensions.scss';

#main-footer {
  display: block;
  background-color: $color-blue-heavy;
  padding: 50px 0 0 0;
  .footer-menus {
    justify-content: center;
    display: flex;
    width: 100%;
    margin: 60px 0 0 0;
  }
  .footer-info {
    text-align: center;
    margin: 60px 0 0 0;
    p, .footer-info-cta {
      margin: 4px 0;
      color: #fff;
      display: block;
    }
    .footer-info-cta {
      text-decoration: none;
      &:hover {
        color: $color-green-light;
      }
    }
    .social-nav {
      display: block;
      margin-top: 20px;
      a {
        text-decoration: none;
        @extend %circle-icon;
        padding: 8px 10px;
        margin: 0 3px;
        background-color: $color-blue-black;
        color: #fff;
        @include transition($transition);
        &:hover {
          background-color: $color-green-light;
          color: $color-green-dark;
        }
      }
    }
  }
  .lower-footer {
    background-color: $color-blue-black;
    color: #fff;
    font-size: 15px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px 0;
    margin: 40px 0 38px 0;
    p {
      margin: 0;
      padding: 0;
      i,
      span {
        color: $color-green-light;
      }
    }
  }
}

@media (min-width: 992px) {
  #main-footer {
    .lower-footer {
      margin-bottom: 0;
    }
  }
}
</style>
