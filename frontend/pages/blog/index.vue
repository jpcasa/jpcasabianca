<template>
  <section>

    <section id="blog">
      <div class="container">
        <SimpleTitle
          id="blog-title"
          class="text-center"
          title="Blog"
          subtitle="My Medium Stories"
          copy="I read a lot of stuff every week and love to stay up to date with everything happening. Sometimes it’s overwhelming, so I usually pin out the most important news of the week with a newsletter."
          theme="light" />
        <SubscribeSimple id="subscribe-simple" />
      </div>
      <BlogSlider id="blog-slider" />
      <div class="text-center cta-blog">
        <a href="#" class="cta">See All Articles</a>
      </div>
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
@import '~/assets/css/helpers/_extensions.scss';

#blog {
  padding-top: 70px;
  background-color: $color-gray-light;
  .subtitle {
    margin-top: 0;
  }
  .cta-blog {
    padding-bottom: 50px;
    .cta {
      display: inline-block;
      margin: auto;
      @extend %background-green;
      @extend %cta;
    }
  }
}

#subscribe-simple {
  margin-bottom: 40px;
}

#blog-slider {
  padding-bottom: 50px;
}
</style>
