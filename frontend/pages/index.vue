<template>
  <section>

    <!-- FIRST FOLD -->
    <section id="section-first-fold">
      <div class="container">
        <DynamicTitleWithCta
          id="title-with-cta1"
          title="I’m a Full Stack Developer and "
          :words="['design cool shit', 'totally into APIs', 'less is more', 'love star wars']"
          subtitle="Hi There"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          cta="Discover Me"
          ctaUrl="section-short-bio"
          action="scroll" />
        <img src="img/computer.png" alt="Computer">
      </div>
    </section>

    <!-- SECTION SHORT BIO -->
    <section id="section-short-bio">
      <div class="container">
        <ImgTitleWithCta
          title="I’m a Full Stack Developer and "
          subtitle="Hi There"
          img=""
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          cta="Discover Me"
          ctaUrl="section-skills"
          action="scroll"
          className="dark" />
        </div>
    </section>

    <!-- SECTION SKILLS -->
    <section id="section-skills">
      <div class="container">
        <TitleWithCta
          title="I’m a Full Stack Developer and "
          subtitle="Hi There"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          cta="Discover Me"
          ctaUrl="section-skills"
          action="scroll" />
        <TabsFull :items="skillCategories" :active="url" @clicked="searchSkills" />
        <DotChart :items="skillsCat" />
      </div>
    </section>

    <!-- SECTION EXPERIENCE -->
    <section id="section-experience">
      <div class="container text-center">
        <SimpleTitle
          title="Experience &amp; Work"
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          theme="light" />
        <span class="flashing-title">Swipe Right<i class="icon-arrow-right"></i></span>
      </div>
      <Timeline />
    </section>

    <!-- SECTION PROGRAMS -->
    <section id="section-programs">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-programs"
          title="Program Master"
          subtitle="Some programs I use"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          theme="light" />
        <div class="programs-flex">
          <FilterDropdown
            id="filter-programs"
            icon="arrow"
            title="Filter Programs" />
          <HorizontalCards />
        </div>
      </div>
    </section>

    <section id="section-education">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-education"
          title="Education"
          subtitle="Courses &amp; Education"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          theme="light" />
        <div class="img-cards">
          <ImgCard v-for="i in (0,5)" :key="i" />
        </div>
      </div>
    </section>

    <section id="section-courses">
      <section id="courses">
        <div class="container text-center">
          <SimpleTitle
            id="simple-title-courses"
            title="Courses"
            subtitle="Some programs I use"
            copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
            theme="light" />
            <span class="flashing-title">Swipe Right<i class="icon-arrow-right"></i></span>
        </div>
        <CardSlider />
      </section>
      <section id="section-testimonies">
        <div class="container text-center">
          <SimpleTitle
            id="simple-title-testimonies"
            title="Testimonies"
            subtitle="Some programs I use"
            copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
            theme="light" />
          <div class="profile-card-container">
            <ProfileCard v-for="i in (0, 3)" :key="i" />
          </div>
        </div>
      </section>
    </section>

  </section>
</template>

<script>
import DynamicTitleWithCta from '~/components/Elements/Titles/DynamicTitleWithCta.vue'
import ImgTitleWithCta from '~/components/Elements/Titles/ImgTitleWithCta.vue'
import TitleWithCta from '~/components/Elements/Titles/TitleWithCta.vue'
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue'
import TabsFull from '~/components/Navigation/Tabs/TabsFull.vue'
import DotChart from '~/components/Elements/Charts/DotChart.vue'
import Timeline from '~/components/Elements/Charts/Timeline.vue'
import FilterDropdown from '~/components/Navigation/Dropdowns/FilterDropdown.vue'
import HorizontalCards from '~/components/Elements/Cards/HorizontalCards.vue'
import ImgCard from '~/components/Elements/Cards/ImgCard.vue'
import CardSlider from '~/components/Sliders/CardSlider.vue'
import ProfileCard from '~/components/Elements/Cards/ProfileCard.vue'


export default {
  data() {
    return {
      url: "frontend"
    }
  },
  components: {
    DynamicTitleWithCta,
    ImgTitleWithCta,
    TitleWithCta,
    SimpleTitle,
    TabsFull,
    DotChart,
    Timeline,
    FilterDropdown,
    HorizontalCards,
    ImgCard,
    CardSlider,
    ProfileCard
  },
  computed: {
    skillCategories() {
      return this.$store.state.skills.skill_categories
    },
    skills() {
      return this.$store.state.skills.skills
    },
    skillsCat() {
      return this.$store.state.skills.skills_cat
    },
  },
  methods: {
    searchSkills(url) {
      this.url = url
      this.searchSkillsApi(url)
    },
    searchSkillsApi(url) {
      this.$store.dispatch('skills/getSkillsCat', url)
    }
  },
  created() {
    this.$store.dispatch('skills/getSkillCategories')
    this.$store.dispatch('skills/getSkills')
    this.searchSkillsApi(this.url)
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

#section-first-fold {
  background-image: url('~/static/img/section-first-fold.png');
  background-size: cover;
  background-position: bottom;
  padding: 70px 0 100px 0;
  display: flex;
  flex-direction: column;
  text-align: center;
  position: relative;
  #title-with-cta1 {
    margin-bottom: 30px;
  }
}

#section-short-bio {
  text-align: center;
  display: flex;
  width: 100%;
  margin: 30px 0 0px 0;
  z-index: 100;
}

#section-skills {
  background-image: url('~/static/img/section-skills.png');
  background-size: cover;
  background-position: right;
  text-align: center;
  display: block;
  z-index: 50;
  .title-with-cta {
    padding: 300px 0 40px 0;
  }
  .tabs-full {
    margin-bottom: 20px;
  }
  .dot-chart {
    padding-bottom: 180px;
  }
}

#section-experience {
  background-image: url('~/static/img/section-exp.png');
  background-size: cover;
  background-position: left;
  z-index: 45;
  padding-bottom: 280px;
  .flashing-title {
    color: $color-green;
    font-family: $proxima-nova-bold;
    display: block;
    margin-bottom: 25px;
  }
  .subtitle {
    margin: 0;
  }
}

#section-programs {
  margin-bottom: 50px;
  #simple-title-programs {
    margin-bottom: 25px;
  }
  #filter-programs {
    margin-bottom: 30px;
    p {
      background-color: $color-gray-light;
    }
  }
}

#section-education {
  background-image: url('~/static/img/section-education.png');
  background-size: cover;
  background-position: right;
  #simple-title-education {
    margin-bottom: 50px;
  }
}

#section-courses {
  background-image: url('~/static/img/section-courses.png');
  background-size: cover;
  background-position: right;
  margin-top: 60px;
  .flashing-title {
    color: $color-green;
    margin-bottom: 60px;
  }
  #simple-title-courses {
    padding-top: -50px;
  }
}

#courses {
  margin-bottom: 60px;
}

#section-testimonies {
  #simple-title-testimonies {
    margin-bottom: 40px;
  }
  padding-bottom: 50px;
}

@media (min-width: 768px) {
  #section-education {
    .img-cards {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      .img-card {
        width: 250px;
        margin: 0 10px 25px 10px;
      }
    }
  }
  #section-first-fold {
    img {
      width: 600px;
      height: auto;
      margin: auto;
    }
  }
}

@media (min-width: 992px) {
  #section-first-fold {
    height: 500px!important;
    background-color: none;
    padding-top: 20px;
    .container {
      display: flex;
      #title-with-cta1 {
        flex: 2;
        text-align: left;
      }
      img {
        flex: 3;
        text-align: left;
        max-width: 500px;
      }
    }
  }

  #section-programs {
    .programs-flex {
      display: flex;
    }
    #filter-programs {
      flex: 1;
      margin-right: 25px;
      span, p {
        display: none;
      }
    }
    .horizontal-cards {
      flex: 2;
    }
  }

  #section-testimonies {
    .container {
      display: flex;
      #simple-title-testimonies {
        flex: 2;
        text-align: left;
        margin-right: 25px;
      }
      .profile-card-container {
        flex: 3;
      }
    }
  }
}
</style>
