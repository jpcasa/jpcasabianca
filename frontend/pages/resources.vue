<template>
  <section>

    <section id="stay-to-date">
      <div class="container">
        <SimpleTitle
          class="text-center"
          id="simple-title-resources"
          title="Are you into APIs too? I use them all the time..."
          subtitle="Some programs I use"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          theme="light" />
        <ResourceCard />
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
}
</style>
