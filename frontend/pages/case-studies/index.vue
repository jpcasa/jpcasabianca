<template>
  <section id="cases">

    <section id="case-studies-top">
      <div class="container mobile">
        <SimpleTitle
          id="simple-title-case-top"
          class="text-center"
          title="I Love Creating and Building Cool Stuff"
          subtitle="Creative process in action"
          copy=""
          theme="light" />
      </div>
      <img src="img/case-studies-top.png" alt="Case Studies Top" class="mobile">
      <div class="container text-center mobile">
        <p class="copy">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
        <p class="copy">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
      </div>
      <div class="case-studies-desktop">
        <SimpleTitle
          id="simple-title-case-top-desktop"
          class="text-center"
          title="I Love Creating and Building Cool Stuff"
          subtitle="Creative process in action"
          copy='Nothing is cooler than the real thing. You can check out my <a href="https://dribbble.com/jpcasabianca" target="_blank">Dribbble</a> account if you want to see my design work. To check out some public stuff I’ve made go to <a href="https://github.com/jpcasa" target="_blank">Github</a> or <a href="https://bitbucket.org/jpcasabianca/" target="_blank">Bitbucket</a>. If you’re looking for the complete story scroll down.'
          theme="light" />
        <div class="case-studies-desktop-img">
          <img src="img/case-studies-top-desktop.png" alt="Case Studies JP Casabianca" class="desktop" id="simple-title-case-img">
        </div>
      </div>
    </section>

    <section id="printa-delivery">
      <div class="container">
        <PortfolioCard class="mobile" />
      </div>
      <div class="portfolio-flex desktop">
        <div class="portfolio-card-flex" id="printa-back">
          <PortfolioCardSimple
            :url="$store.state.portfolio.case_studies[0].url"
            :title="$store.state.portfolio.case_studies[0].title"
            :tags="$store.state.portfolio.case_studies[0].tags" />
        </div>
        <TitleWithCta
          id="portfolio-printa"
          class="padding-right"
          :title="$store.state.portfolio.case_studies[0].title"
          :subtitle="$store.state.portfolio.case_studies[0].subtitle"
          :copy='$store.state.portfolio.case_studies[0].summary'
          :cta="$store.state.portfolio.case_studies[0].cta"
          :ctaUrl="'/case-studies/' + $store.state.portfolio.case_studies[0].url"
          action="push"
          theme="light" />
      </div>
    </section>

    <section id="mapps360">
      <div class="container">
        <PortfolioCard class="mobile" />
      </div>
      <div class="portfolio-flex desktop">
        <TitleWithCta
          id="portfolio-printa"
          class="padding-left"
          :title="$store.state.portfolio.case_studies[1].title"
          :subtitle="$store.state.portfolio.case_studies[1].subtitle"
          :copy='$store.state.portfolio.case_studies[1].summary'
          :cta="$store.state.portfolio.case_studies[1].cta"
          :ctaUrl="'/case-studies/' + $store.state.portfolio.case_studies[1].url"
          action="push"
          theme="light" />
        <div class="portfolio-card-flex" id="codesign-back">
          <PortfolioCardSimple
            :url="$store.state.portfolio.case_studies[1].url"
            :title="$store.state.portfolio.case_studies[1].title"
            :tags="$store.state.portfolio.case_studies[1].tags" />
        </div>
      </div>
    </section>
  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue'
import TitleWithCta from '~/components/Elements/Titles/TitleWithCta.vue'
import PortfolioCard from '~/components/Elements/Cards/PortfolioCard.vue'
import PortfolioCardSimple from '~/components/Elements/Cards/PortfolioCardSimple.vue'

export default {
  components: {
    SimpleTitle,
    TitleWithCta,
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
  .simple-title,
  .title-with-cta {
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
  min-height: 600px;
}

#codesign-back {
  background-image: url('~/static/img/codesign-back.png');
  background-size: cover;
  background-position: right;
  min-height: 600px;
}

#mapps360-back {
  background-image: url('~/static/img/mapps360-back.png');
  background-size: cover;
  background-position: left;
  min-height: 600px;
}

.case-studies-desktop {
  align-items: center;
  display: none;
  #simple-title-case-top-desktop {
    flex: 2;
    margin-left: 50px;
    text-align: left;
  }
  .case-studies-desktop-img {
    flex: 3;
  }
}

@media (min-width: 992px) {
  #case-studies-top {
    display: flex;
    padding-top: 0;
    align-items: center;
  }
  .case-studies-desktop {
    display: flex;
  }
}
</style>
