<template>
  <section>

    <section id="tech-stack">
      <div class="container">
        <SimpleTitle
          class="text-center text-capitalize"
          id="simple-title-tech-stack"
          :title="'My ' + title + ' skills'"
          subtitle="My Tech Stack"
          copy=""
          theme="light" />
        <div class="search">
          <i class="icon-search"></i>
          <input type="search" placeholder="Enter programming language, framework, plugin, etc..." v-model="query" />
        </div>
        <div class="choices text-center">
          <span class="text-center"><i class="icon-star"></i> Preferred Choices</span>
        </div>
        <div class="skill-cards">
          <SkillCard v-for="(skill, index) in skills" :key="index" :skill="skill" />
        </div>
      </div>
    </section>

  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue'
import FilterDropdown from '~/components/Navigation/Dropdowns/FilterDropdown.vue'
import SkillCard from '~/components/Elements/Cards/SkillCard.vue'

export default {
  data() {
    return {
      query: null
    }
  },
  components: {
    SimpleTitle,
    FilterDropdown,
    SkillCard
  },
  computed: {
    skills() {
      if (this.query && this.query.length > 2) {
        return this.$store.state.skills.skills_cat.filter(
          item => item.name.toLowerCase().includes(this.query.toLowerCase())
        )
      } else {
        return this.$store.state.skills.skills_cat
      }
    },
    title() {
      return this.$route.params.url
    }
  },
  created() {
    this.$store.dispatch('skills/getSkillsCat', this.$route.params.url)
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

.text-capitalize {
  text-transform: capitalize;
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
