<template>
  <section>

    <section id="tech-stack">
      <div class="container">
        <SimpleTitle
          class="text-center"
          id="simple-title-tech-stack"
          title="Are you into APIs too? I use them all the time..."
          subtitle="Some programs I use"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          theme="light" />
        <div class="search">
          <i class="icon-search"></i>
          <input type="search" placeholder="Enter programming language, framework, plugin, etc..." />
        </div>
        <FilterDropdown
          id="filter-programs"
          icon="arrow"
          title="Filter Programs" />
        <div class="choices text-center">
          <span class="text-center"><i class="icon-star"></i> Preferred Choices</span>
        </div>
        <div class="skill-cards">
          <SkillCard v-for="i in (0, 1)" :key="i" />
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
  components: {
    SimpleTitle,
    FilterDropdown,
    SkillCard
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
}

.skill-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
