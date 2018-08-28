<template>
  <div>

    <header id="desktop-sidebar">
      <nuxt-link to="/">JP Casabianca</nuxt-link>
      <ul>
        <li>About Me</li>
        <li>Creative Process</li>
        <li>My Tech Stack</li>
        <li>Case Studies</li>
        <li>Resources</li>
        <li>Blog</li>
      </ul>
      <div class="contact-menu">
        <div class="menu-row">
          <p>Important Stuff</p>
          <a href="#">Resume</a>
        </div>
        <div class="menu-row">
          <p>Contact</p>
          <a href="#">hola@jpcasabianca.com</a>
          <a href="#">+57 350 701 5800</a>
        </div>
        <div class="menu-row">
          <p>Find me on</p>
          <a href="#">Linkedin</a>
          <a href="#">Medium</a>
        </div>
        <div class="menu-row">
          <p>Version Control</p>
          <a href="#">Github</a>
          <a href="#">Bitbucket</a>
        </div>
      </div>
    </header>

    <!-- MAIN CONTENT -->
    <main>

      <!-- HEADERS -->
      <span class="icon-menu" id="menu-icon"></span>
      <span class="icon-message-square" id="contact-icon"></span>

      <section id="page-section">

        <!-- PAGE CONTENT -->
        <nuxt/>

        <!-- FOOTER -->
        <footer id="main-footer">
          <span>Main Footer</span>
        </footer>

      </section>
    </main>

    <ul id="navigation-mobile">
      <li class="active">
        <i class="icon-map-pin"></i>
        <span>Skills</span>
      </li>
      <li>
        <i class="icon-map-pin"></i>
        <span>Education</span>
      </li>
      <li>
        <i class="icon-map-pin"></i>
        <span>Programs</span>
      </li>
      <li>
        <i class="icon-map-pin"></i>
        <span>Experience</span>
      </li>
      <li>
        <i class="icon-map-pin"></i>
        <span>Testimonies</span>
      </li>
    </ul>

  </div>
</template>

<style lang="scss" scoped>
@import '../assets/css/helpers/_variables.scss';
@import '../assets/css/helpers/_extensions.scss';

main {
  position: relative;
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

#page-section {
  display: flex;
  height: 450px;
  background-color: $color-gray-light;
}

#navigation-mobile {
  display: flex;
  position: fixed;
  z-index: 190;
  width: 100%;
  bottom: 0;
  left: 0;
  background-color: $color-blue-black;
  text-align: center;
  padding: 0;
  margin: 0;
  list-style: none;
  li {
    flex: 1;
    color: $color-gray;
    padding: 0;
    margin: 0;
    padding: 5px 0;
    cursor: pointer;
    i,
    span {
      display: block;
    }
    i {
      margin-bottom: 4px;
    }
    span {
      font-size: 10px;
      font-family: $gotham-rounded-book;
    }
    &:hover {
      background-color: $color-green-light;
      color: $color-green-dark;
    }
  }
  .active {
    background-color: $color-green-light;
    color: $color-green-dark;
  }
}

#desktop-sidebar {
  width: $sidebar-width;
  height: 100vh;
  position: fixed;
  left: 0;
  background-color: $color-red;
}

@media (min-width: 600px) {
  #navigation-mobile {
    li {
      span {
        font-size: 13px;
      }
      i {
        font-size: 18px;
      }
    }
  }
}

@media (min-width: 992px) {
  #navigation-mobile {
    display: none;
  }
  #menu-icon,
  #contact-icon {
    display: none;
  }
  #page-section {
    margin-left: $sidebar-width;
  }
}
</style>
