<template>
  <div>

    <!-- MAIN CONTENT -->
    <main>

      <!-- HEADERS -->
      <span class="icon-menu" id="menu-icon"></span>
      <span class="icon-message-square" id="contact-icon"></span>

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
    <MobileNav />

    <!-- DESKTOP HEADER -->
    <SidebarHeader />

  </div>
</template>

<script>
import SidebarHeader from '~/components/Headers/SidebarHeader.vue'
import MobileNav from '~/components/Navigation/MobileNav.vue'
import CompleteFooter from '~/components/Footers/CompleteFooter.vue'

export default {
  components: {
    SidebarHeader,
    MobileNav,
    CompleteFooter
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
    background-color: $color-gray-light;
  }
}

#menu-icon,
#contact-icon {
  @extend %circle-icon;
  @extend %background-green;
  position: fixed;
  z-index: 200;
  top: 16px;
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

@media (min-width: 992px) {
  #menu-icon,
  #contact-icon {
    display: none;
  }
  #page-section {
    margin-left: $sidebar-width;
  }
}
</style>
