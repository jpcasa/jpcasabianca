<template lang="html">
  <h2 class="title">
    <span>{{ title }}</span>
    <span class="changing-color">{{ text }}.</span>
  </h2>
</template>

<script>
export default {
  props: ['title', 'words'],
  data() {
    return {
      text: "",
      count: 0
    }
  },
  methods: {
    getWord() {
      if (this.count < (this.words.length - 1)) {
        this.count += 1
      } else {
        this.count = 0
      }
    },
    changeWord() {
      setInterval(() => {
        this.getWord()
        this.text = this.words[this.count]
      }, 3000)
    }
  },
  mounted() {
    this.text = this.words[this.count]
    this.changeWord()
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_extensions.scss';

.title {
  .changing-color {
    color: $color-green-light;
  }
}
</style>
