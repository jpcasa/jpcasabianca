<template lang="html">
  <div class="color-palette">
    <div class="color-palette-cont" v-for="(color, index) in colors" :key="index">
      <p>{{ color.title }}</p>
      <div class="color-palette-low" :style="palette_style(color)">
        <ul>
          <li>C: {{ color.cmyk.c }}</li>
          <li>M: {{ color.cmyk.m }}</li>
          <li>Y: {{ color.cmyk.y }}</li>
          <li>K: {{ color.cmyk.k }}</li>
        </ul>
        <ul>
          <li>R: {{ color.rgb.r }}</li>
          <li>G: {{ color.rgb.g }}</li>
          <li>B: {{ color.rgb.b }}</li>
        </ul>
        <hr :style="hr_style(color)">
        <ul>
          <li>PANTONE</li>
          <li>{{ color.pantone }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['colors'],
  methods: {
    palette_style(color) {
      return `background-color:${color.hex};
              color:${color.fontColor};
              border:1px solid ${color.border};`
    },
    hr_style(color) {
      return `border:none;
              border-bottom: 1px solid ${color.fontColor};`
    }
  }
}
</script>

<style lang="scss">
.color-palette {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  .color-palette-cont {
    text-align: center;
    width: 130px;
    margin: 0 10px 25px 10px;
    p {
      font-size: 14px;
    }
    .color-palette-low {
      padding: 25px 15px;
      font-size: 15px;
      ul {
        padding: 0;
        list-style: none;
      }
    }
  }
}
</style>
