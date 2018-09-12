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
        <ResourceCard v-for="i in (0, 9)" :key="i" />
      </div>
    </section>

  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue';
import ResourceCard from '~/components/Elements/Cards/ResourceCard.vue';

export default {
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
  padding-top: 70px;
}

#stay-to-date-title {
  margin-bottom: 30px;
}
</style>
