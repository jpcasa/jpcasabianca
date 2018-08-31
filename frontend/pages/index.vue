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
          ctaUrl="section-skills"
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

    <section id="section-skills">
      <div class="container">
        <TitleWithCta
          title="I’m a Full Stack Developer and "
          subtitle="Hi There"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          cta="Discover Me"
          ctaUrl="section-skills"
          action="scroll" />
        <TabsFull :items="skillCategories" />
        <DotChart />
      </div>
    </section>

  </section>
</template>

<script>
import DynamicTitleWithCta from '~/components/Elements/Titles/DynamicTitleWithCta.vue'
import ImgTitleWithCta from '~/components/Elements/Titles/ImgTitleWithCta.vue'
import TitleWithCta from '~/components/Elements/Titles/TitleWithCta.vue'
import TabsFull from '~/components/Navigation/Tabs/TabsFull.vue'
import DotChart from '~/components/Elements/Charts/DotChart.vue'

export default {
  components: {
    DynamicTitleWithCta,
    ImgTitleWithCta,
    TitleWithCta,
    TabsFull,
    DotChart
  },
  computed: {
    skillCategories() {
      return this.$store.state.skills.skill_categories
    },
    skills() {
      return this.$store.state.skills.skills
    },
  },
  created() {
    this.$store.dispatch('skills/getSkillCategories')
    this.$store.dispatch('skills/getSkills')
  }
}
</script>

<style lang="scss">
#section-first-fold {
  background-image: url('~/static/img/section-first-fold.png');
  background-size: cover;
  padding: 60px 0 50px 0;
  display: flex;
  flex-direction: column;
  text-align: center;
  #title-with-cta1 {
    margin-bottom: 30px;
  }
}

#section-short-bio {
  text-align: center;
  display: flex;
  width: 100%;
  margin: 30px 0 -60px 0;
}

#section-skills {
  background-image: url('~/static/img/section-skills.png');
  background-size: cover;
  background-position: right;
  text-align: center;
  display: block;
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
</style>
