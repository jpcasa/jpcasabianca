<template>
  <div>

    <!-- MAIN CONTENT -->
    <main>

      <!-- HEADERS -->
      <span @click="showMobileMenu = true" class="icon-menu" id="menu-icon"></span>
      <span @click="toggleMobileContact('open')" class="icon-message-square" id="contact-icon"></span>

      <section id="page-section">

        <div id="main-page-content">
          <!-- PAGE CONTENT -->
          <nuxt/>
        </div>

        <!-- FOOTER -->
        <CompleteFooter />

      </section>
    </main>

    <!-- MOBILE NAVIGATION -->
    <MobileNav :menu="mobileMenu" />

    <transition name="fade">
      <div class="mobile-header" v-if="showMobileMenu">
        <i class="icon-x-circle" @click="showMobileMenu = false"></i>
        <nuxt-link
          v-for="(item, index) in mainMenu.menu_items"
          :key="index"
          :to="'/' + item.url"
          @click.native="activateMenu(item.id)">
          {{ item.title }}
        </nuxt-link>
        <a href="https://medium.com/@jpc_774" target="_blank">Blog</a>
      </div>
    </transition>

    <transition name="fade">
      <div class="mobile-contact-info" v-if="showMobileInfo">
        <i class="icon-x-circle" @click="toggleMobileContact('close')" id="close-contact-info"></i>
        <MobileContact :menu="contactMenu.menu_items" />
      </div>
    </transition>

    <!-- DESKTOP HEADER -->
    <SidebarHeader
      :menu="mainMenu.menu_items"
      :contact="contactMenu.menu_items" />

    <a v-show="showMessageIcons" href="#" id="contact-whatsapp">
      <img src="~/static/img/whatsapp.svg" />
    </a>

    <a v-show="showMessageIcons" href="#" id="contact-fb">
      <img src="~/static/img/fb-messenger.svg" />
    </a>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import SidebarHeader from '~/components/Headers/SidebarHeader.vue'
import MobileNav from '~/components/Navigation/MobileNav.vue'
import CompleteFooter from '~/components/Footers/CompleteFooter.vue'
import MobileContact from '~/components/Elements/MobileContact.vue'

export default {
  data() {
    return {
      showMobileMenu: false,
      showMobileInfo: false,
      showMessageIcons: true
    }
  },
  computed: {
    mainMenu() {
      return this.$store.state.menus.menu
    },
    contactMenu() {
      return this.$store.state.menus.contactMenu
    },
    mobileMenu() {
      return this.$store.state.menus.subMenu
    }
  },
  components: {
    SidebarHeader,
    MobileNav,
    CompleteFooter,
    MobileContact
  },
  methods: {
    activateMenu(id) {
      this.$store.dispatch('menus/getSubMenu', id)
      this.showMobileMenu = false
    },
    toggleMobileContact(action) {
      if (action == 'open') {
        this.showMobileInfo = true
        this.showMessageIcons = false
      } else {
        this.showMobileInfo = false
        this.showMessageIcons = true
      }
    }
  },
  created() {

    this.$axios.setHeader("Content-Type", "application/x-www-form-urlencoded", [
      "post"
    ])
    this.$axios.setToken("6b04a68e84b72c9d24a7340316e25d990d2bbba3", "Token")

    this.$store.dispatch('menus/getMainMenu', this.$nuxt.$route.path)
    this.$store.dispatch('menus/getContactMenu')

    // Skills
    this.$store.dispatch('skills/getSkillCategories')
    this.$store.dispatch('skills/getSkills')
    this.$store.dispatch('skills/getSkillsCat', 'frontend')

    // Experience
    this.$store.dispatch('experiences/getExperience')

    // Programs
    this.$store.dispatch('programs/getPrograms')
    this.$store.dispatch('programs/getProgramCategories')
    this.$store.dispatch('programs/getProgramsCat', 'business-and-finance')

    // Education
    this.$store.dispatch('education/getEducation')

    // Courses
    this.$store.dispatch('education/getCourses')

    // Portfolio
    this.$store.dispatch('portfolio/getCaseStudies')
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

main {
  position: relative;
  #page-section {
    display: block;
    height: 450px;
  }
}

#menu-icon,
#contact-icon {
  @extend %circle-icon;
  @extend %background-green;
  position: fixed;
  z-index: 200;
  top: 20px;
  font-size: 20px;
  cursor: pointer;
}

#menu-icon {
  left: 20px;
}

#contact-icon {
  right: 20px;
}

#main-page-content {
  display: block;
}

.mobile-contact-info {
  z-index: 350;
  position: fixed;
  height: 100vh;
  width: 100vw;
  left: 0;
  top: 0;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  #close-contact-info {
    position: absolute;
    right: 20px;
    top: 20px;
    font-size: 36px;
    color: #fff;
    cursor: pointer;
  }
  .upper-info {
    background-image: url('/img/mobile.jpg');
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
            i, span {
              display: block;
              color: $color-gray-heavy;
            }
            span {
              margin-top: 4px;
              font-size: 12px;
              font-family: $proxima-nova;
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
        }
        span {
          color: $color-gray-heavy;
        }
        a {
          text-decoration: none;
          display: inline-block;
          padding: 9px 45px;
          font-family: $gotham-rounded-medium;
          font-size: 14px;
          @include border-radius($border-radius);
          @extend %background-green;
          margin-top: 10px;
        }
      }
    }
  }
}

.mobile-header {
  z-index: 300;
  position: fixed;
  height: 100vh;
  width: 100vw;
  left: 0;
  top: 0;
  background-color: $color-green-light;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  @include transition($transition);
  i {
    position: absolute;
    left: 20px;
    top: 20px;
    z-index: 310;
    cursor: pointer;
    font-size: 36px;
    color: $color-green-dark;
  }
  a {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    text-decoration: none;
    font-size: 20px;
    color: $color-green-dark;
    font-family: $gotham-rounded-medium;
    &:hover {
      background-color: $color-green;
    }
  }
  .nuxt-link-exact-active {
    background-color: $color-green;
  }
}

#contact-whatsapp,
#contact-fb {
  position: fixed;
  bottom: 55px;
  z-index: 1000;
  img {
    width: 35px;
    height: 35px;
  }
}

#contact-whatsapp {
  right: 15px;
}

#contact-fb {
  right: 60px;
}

@media (min-width: 992px) {
  #menu-icon,
  #contact-icon {
    display: none;
  }
  #page-section {
    margin-left: $sidebar-width;
  }
  #contact-whatsapp,
  #contact-fb {
    bottom: 15px;
  }
}
</style>
