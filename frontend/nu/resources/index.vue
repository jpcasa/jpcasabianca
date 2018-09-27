<template>
  <section>

    <section id="stay-to-date">
      <div class="container text-center">
        <SimpleTitle
          id="stay-to-date-title"
          title="Experience &amp; Work"
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          theme="light" />
        <div class="resource-cards-container">
          <ResourceCard v-for="(item, index) in resources" :key="index" :resource="item" />
        </div>
      </div>
    </section>

  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue';
import ResourceCard from '~/components/Elements/Cards/ResourceCard.vue';

export default {
  data() {
    return {
      resources: [
        { 'title': 'Stay up to date', 'icon': 'algo' },
        { 'title': 'Courses', 'icon': 'algo' },
        { 'title': 'Blogs', 'icon': 'algo' },
        { 'title': 'Podcasts', 'icon': 'algo' },
        { 'title': 'Repos', 'icon': 'algo' },
        { 'title': 'Productivity', 'icon': 'algo' },
        { 'title': 'Newsletters', 'icon': 'algo' },
        { 'title': 'Inspiration', 'icon': 'algo' },
        { 'title': 'Books', 'icon': 'algo' }
      ]
    }
  },
  components: {
    SimpleTitle,
    ResourceCard
  }
}
</script>

<style lang="scss">
#stay-to-date {
  background-image: url('~/static/img/resources.png');
  background-size: cover;
  background-position: left;
  padding: 70px 0;
}

#stay-to-date-title {
  margin-bottom: 30px;
}

@media (min-width: 768px) {
  #stay-to-date {
    .resource-cards-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      .resource-card {
        width: 250px;
        margin: 0 10px 25px 10px;
      }
    }
  }
}

@media (min-width: 900px) {
  #stay-to-date-title {
    display: none;
  }
}
</style>
