<template>
  <section>

    <section id="tech-stack">
      <div class="container">
        <SimpleTitle
          class="text-center"
          id="simple-title-tech-stack"
          title="Are you into Vue.js too? Django is just awesome…"
          subtitle="My Tech Stack"
          copy="Here is a list of languages, libraries, and frameworks I’ve used and worked with. Feel free to explore!"
          theme="light" />
        <div class="search">
          <i class="icon-search"></i>
          <input type="search" placeholder="Enter programming language, framework, plugin, etc..." v-model="query" />
        </div>
        <div class="choices text-center">
          <span class="text-center"><i class="icon-star"></i> Preferred Choices</span>
        </div>
        <div class="skill-cards">
          <SkillCard
            v-for="(skill, index) in skills"
            :key="index"
            :skill="skill"
            @clicked="showSkillDetail" />
        </div>
        <transition name="fade">
          <SkillCardDetail v-show="skill_detail" :skill="detail" @clicked="closeDetail" />
        </transition>
      </div>
    </section>

  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue'
import FilterDropdown from '~/components/Navigation/Dropdowns/FilterDropdown.vue'
import SkillCard from '~/components/Elements/Cards/SkillCard.vue'
import SkillCardDetail from '~/components/Elements/Cards/SkillCardDetail.vue'

export default {
  data() {
    return {
      query: null,
      skill_detail: false,
      detail: this.$store.state.skills.skills
    }
  },
  components: {
    SimpleTitle,
    FilterDropdown,
    SkillCard,
    SkillCardDetail
  },
  computed: {
    skills() {
      if (this.query && this.query.length > 2) {
        return this.$store.state.skills.skills.filter(
          item => item.name.toLowerCase().includes(this.query.toLowerCase())
        )
      } else {
        return this.$store.state.skills.skills
      }
    }
  },
  methods: {
    showSkillDetail(skill) {
      this.detail = skill
      this.skill_detail = true
    },
    closeDetail() {
      this.skill_detail = false
    }
  },
  created() {
    this.$store.dispatch('skills/getSkills')
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

#tech-stack {
  display: block;
  width: 100%;
  background-image: url('~/static/img/tech-stack.png');
  background-size: cover;
  background-position: left;
  padding-bottom: 50px;
  .choices {
    span {
      font-size: 13px;
      font-family: $proxima-nova;
      color: $color-gray-heavy;
      i {
        color: $color-green;
      }
    }
  }
}

#simple-title-tech-stack {
  padding-top: 80px;
  .subtitle {
    margin: 0 0 10px 0;
  }
}

.search {
  margin-bottom: 40px;
  position: relative;
  .icon-search {
    position: absolute;
    left: 10px;
    top: 12px;
    color: $color-green;
  }
  input[type="search"] {
    width: 100%;
    border: none;
    height: 40px;
    font-size: 14px;
    @include border-radius($border-radius);
    font-family: $proxima-nova;
    text-indent: 32px;
  }
}

#filter-programs {
  p {
    background-color: #fff;
    &:hover {
      background-color: $color-green-light;
    }
  }
  .filter-dropdown-container {
    background-color: #fff;
  }
  .desktop-list {
    display: none;
  }
}

.skill-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
