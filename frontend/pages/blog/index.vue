<template>
  <section>

    <section id="blog">
      <div class="container">
        <SimpleTitle
          id="blog-title"
          class="text-center"
          title="Experience &amp; Work"
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
          theme="light" />
        <SubscribeSimple id="subscribe-simple" />
      </div>
      <BlogSlider id="blog-slider" />
    </section>

  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue'
import SubscribeSimple from '~/components/Forms/SubscribeSimple.vue'
import BlogSlider from '~/components/Sliders/BlogSlider.vue'

export default {
  components: {
    SimpleTitle,
    SubscribeSimple,
    BlogSlider
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

#blog {
  padding-top: 70px;
  background-color: $color-gray-light;
  .subtitle {
    margin-top: 0;
  }
}

#subscribe-simple {
  margin-bottom: 40px;
}

#blog-slider {
  padding-bottom: 50px;
}
</style>
