<template>
  <section>

    <!-- FIRST FOLD -->
    <section id="section-first-fold">
      <div class="container">
        <DynamicTitleWithCta
          id="title-with-cta1"
          title="I’m a Full Stack Developer and "
          :words="['Design Cool Stuff', 'Dig Vue and React', 'Totally Into Python', 'Less is More', 'Create Python & JS APIs', 'Know Inbound Marketing', 'Love Star Wars & GOT' , 'Worked in Finance', 'Play Zelda & Mario']"
          subtitle="Hi There"
          copy="The digital world is crazy, but isn’t that craziness awesome? I strive to find the best and most efficient solutions to the most complex of problems.<br><br> Not only do I apply this to development, but to design and marketing as well. Do you love tech and Star Wars too?"
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
          title="Hi Stranger!"
          subtitle="How you doin’?"
          img=""
          copy='I’ve been developing and designing since 2010. It’s incredible how everything has changed since then. I started off with a traditional frontend stack (HTML, CSS, jQuery) and backend (PHP and MYSQL). <br><br>After a couple of years, I’ve migrated to an awesome frontend stack <span class="color-green">Vue.js, React</span>. And the most beautiful backend there is <span class="color-green">Python, Django</span>. I dig <span class="color-green">Node.js</span> and <span class="color-green">Express</span> too... Feel free to see my complete tech stack <a href="/my-tech-stack">here</a>.'
          cta="Check Out My Skills"
          ctaUrl="section-skills"
          action="scroll"
          className="dark" />
        </div>
    </section>

    <!-- SECTION SKILLS -->
    <section id="section-skills">
      <div class="container">
        <TitleWithCta
          title="Check out my skills"
          subtitle="What are you looking for?"
          copy='"Follow your dreams and use your natural-born talents and skills to make this a better world for tomorrow" - Paul Watson. When you need to get something done, you also know what skills are required to complete the task. I put my heart and mind into my work, so check out my skills and don’t forget to <a href="mailto:hola@jpcasabianca">shoot me an email</a>.'
          cta="See my Experience"
          ctaUrl="section-experience"
          action="scroll"
          theme="dark" />
        <TabsFull :items="skillCategories" :active="url" @clicked="searchSkills" />
        <DotChart :items="skillsCat" />
      </div>
    </section>

    <!-- SECTION EXPERIENCE -->
    <section id="section-experience">
      <div class="container text-center">
        <SimpleTitle
          title="My career and experience"
          subtitle="My version of a Short Story"
          copy='I started developing in 2010 but decided to major in Business. I really wanted to understand the “business” side of things to have a better scope and understanding of real life. Soft skills are equally important as hard skills, so check out my version of a short story. See my full experience <a href="#resume" target="_blank">here</a>.'
          theme="light" />
        <span class="flashing-title">Swipe Right<i class="icon-arrow-right"></i></span>
      </div>
      <!-- <Timeline :items="$store.state.experiences.experiences" /> -->
    </section>

    <!-- SECTION PROGRAMS -->
    <section id="section-programs">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-programs"
          title="One Program to Rule Them All"
          subtitle="Some programs I use"
          copy="The first thing I do every morning is open Station, I fell in love with their slogan “One app to rule them all”. I add all of the apps and programs I normally use to Station and take it from there. If you choose programs wisely you can optimize and improve your work. What programs do you use?"
          theme="light" />
        <div class="programs-flex">
          <FilterDropdown
            id="filter-programs"
            icon="arrow"
            title="Filter Programs"
            :items="programCategories"
            :active="program_url"
            @clicked="searchPrograms" />
          <HorizontalCards :items="programsCat" />
        </div>
      </div>
    </section>

    <section id="section-education">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-education"
          title="My Education"
          subtitle='“You know nothing John Snow”'
          copy="Education is important as hell. Education shapes your way of thought and how you process and analyze information. Check out where I received mine!"
          theme="light" />
        <div class="img-cards">
          <ImgCard v-for="(item, index) in education" :key="index" :item="item" />
        </div>
      </div>
    </section>

    <section id="section-courses">
      <section id="courses">
        <div class="container text-center">
          <SimpleTitle
            id="simple-title-courses"
            title="Courses &amp; Certifications"
            subtitle="Stay up to date"
            copy="The most important thing for every developer and designer is to stay up to date with the latest. With coding changing at an incredible rate, courses are a nice and reliable way to learn new stuff. What courses have you taken lately?"
            theme="light" />
            <span class="flashing-title">Swipe Right<i class="icon-arrow-right"></i></span>
        </div>
        <CardSlider :items="courses" />
      </section>
      <section id="section-testimonies">
        <div class="container text-center">
          <SimpleTitle
            id="simple-title-testimonies"
            title="Testimonies"
            subtitle="What people are saying"
            copy="Isn’t nice when you do a good job, and someone puts in a good word for you? <br><br> These are some happy clients and stakeholders, take a look at their experience."
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
      url: "frontend",
      program_url: "business-and-finance"
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
    experiences() {
      return this.$store.state.experiences.experiences
    },
    programs() {
      return this.$store.state.programs.programs
    },
    programCategories() {
      return this.$store.state.programs.categories
    },
    programsCat() {
      return this.$store.state.programs.programs_cat
    },
    education() {
      return this.$store.state.education.education
    },
    courses() {
      return this.$store.state.education.courses
    }
  },
  methods: {
    searchSkills(url) {
      this.url = url
      this.searchSkillsApi(url)
    },
    searchSkillsApi(url) {
      this.$store.dispatch('skills/getSkillsCat', url)
    },
    searchPrograms(item) {
      this.program_url = item.url
      console.log(item.url)
      this.searchProgramsApi(item.url)
    },
    searchProgramsApi(url) {
      this.$store.dispatch('programs/getProgramsCat', url)
    }
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
    padding-bottom: 280px;
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
  background-image: url('~/static/img/section-education2.png');
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
  margin-top: 80px;
  padding-bottom: 80px;
  .flashing-title {
    color: $color-green;
    padding-bottom: 60px;
    margin-bottom: 0px;
  }
  #simple-title-courses {
    // padding-top: -170px;
  }
}

#courses {
  margin-bottom: 60px;
}

#section-testimonies {
  #simple-title-testimonies {
    // margin-bottom: 40px;
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
    padding: 20px 0 120px 0;
    .container {
      display: flex;
      align-items: center;
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
    #simple-title-programs {
      margin-bottom: 50px;
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
        align-items: flex-start;
        text-align: left;
        margin-right: 25px;
        margin-top: 0;
      }
      .profile-card-container {
        flex: 3;
      }
    }
  }
}
</style>
