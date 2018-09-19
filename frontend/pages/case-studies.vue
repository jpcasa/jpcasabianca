<template>
  <section id="cases">

    <section id="case-studies-top">
      <div class="container mobile">
        <SimpleTitle
          id="simple-title-case-top"
          class="text-center"
          title="I love creating and building cool sh*t."
          subtitle="A short story"
          copy=""
          theme="light" />
      </div>
      <SimpleTitle
        id="simple-title-case-top-desktop"
        class="text-center"
        title="I love creating and building cool sh*t."
        subtitle="A short story"
        copy="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        theme="light" />
      <img src="img/case-studies-top.png" alt="Case Studies Top" class="mobile">
      <img src="img/case-studies-top-desktop.png" alt="Case Studies JP Casabianca" class="desktop">
      <div class="container text-center mobile">
        <p class="copy">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
        <p class="copy">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
      </div>
    </section>

    <section id="printa-delivery">
      <div class="container">
        <PortfolioCard class="mobile" />
      </div>
      <div class="portfolio-flex desktop">
        <div class="portfolio-card-flex" id="printa-back">
          <PortfolioCardSimple />
        </div>
        <SimpleTitle
          id="portfolio-printa"
          class="padding-right"
          title="I love creating and building cool sh*t."
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
          theme="light" />
      </div>
    </section>

    <section id="estudio-codesign">
      <div class="container">
        <PortfolioCard class="mobile" />
      </div>
      <div class="portfolio-flex desktop">
        <SimpleTitle
          id="portfolio-codesign"
          class="padding-left"
          title="I love creating and building cool sh*t."
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
          theme="light" />
        <div class="portfolio-card-flex" id="codesign-back">
          <PortfolioCardSimple />
        </div>
      </div>
    </section>

    <section id="mapps360">
      <div class="container">
        <PortfolioCard class="mobile" />
      </div>
      <div class="portfolio-flex desktop">
        <div class="portfolio-card-flex" id="mapps360-back">
          <PortfolioCardSimple />
        </div>
        <SimpleTitle
          id="portfolio-mapps360"
          class="padding-right"
          title="I love creating and building cool sh*t."
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
          theme="light" />
      </div>
    </section>


  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue'
import PortfolioCard from '~/components/Elements/Cards/PortfolioCard.vue'
import PortfolioCardSimple from '~/components/Elements/Cards/PortfolioCardSimple.vue'

export default {
  components: {
    SimpleTitle,
    PortfolioCard,
    PortfolioCardSimple
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

#cases {
  padding-bottom: 50px;
}

#case-studies-top {
  padding: 70px 0 30px 0;
  #simple-title-case-top {
    .subtitle {
      margin: 0 0 6px 0;
    }
  }
  .copy {
    color: $color-gray-heavy;
  }
}

.portfolio-flex {
  display: flex;
  align-items: center;
  .simple-title {
    flex: 2;
  }
  .portfolio-card-flex {
    flex: 3;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .padding-right {
    padding-right: 50px;
  }
  .padding-left {
    padding-left: 50px;
  }
}

#printa-back {
  background-image: url('~/static/img/printa-back.png');
  background-size: cover;
  background-position: left;
}

#codesign-back {
  background-image: url('~/static/img/codesign-back.png');
  background-size: cover;
  background-position: right;
}

#mapps360-back {
  background-image: url('~/static/img/mapps360-back.png');
  background-size: cover;
  background-position: left;
}

@media (min-width: 992px) {
  #case-studies-top {
    display: flex;
    padding-top: 0;
    align-items: center;
    #simple-title-case-top-desktop {
      flex: 2;
      margin-left: 40px;
      text-align: left;
    }
    img {
      flex: 3;
    }
  }
}
</style>
