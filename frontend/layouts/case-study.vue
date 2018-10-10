<template lang="html">
  <div>

    <main>

      <section id="section-first-fold">
        <div class="first-fold-container">
          <img src="~/static/img/printa-delivery.png" alt="Printa Delivery">
          <h1>Ctrl+P = <span class="helvetica-light-italic">“The Biggest Headache Ever”</span></h1>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
      </section>

      <section id="section-one">
        <div class="cont80 text-center">
          <img src="~/static/img/printa/1.png" alt="" class="image-title">
          <h2 class="section-title">Printing <span class="helvetica-light-italic">Insights</span></h2>
          <div class="icons-container">
            <IconCard
              v-for="(item, index) in section_one"
              :key="index"
              :info="item" />
          </div>
          <div class="messages-cont">
            <p class="titles">Time Consuming</p>
            <p class="titles color-blue">Waste of Time</p>
            <p class="titles color-red">Pain in the Ass</p>
            <p class="titles color-yellow">Low Quality</p>
            <p class="message">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud. </p>
          </div>
        </div>
      </section>

      <section id="section-two">
        <div class="text-center">
          <img src="~/static/img/printa/2.png" alt="" class="image-title">
          <h2 class="section-title">Design <span class="helvetica-light-italic">Process</span></h2>
        </div>
        <div class="timeline-printa" id="timeline-above">
          <div class="half">
            <span class="step">1.0</span>
            <div class="line" />
            <div class="circle circle-black" />
            <span class="title" id="title1">Empathize</span>
          </div>
        </div>
        <div class="cont80 text-center">
          <h2>Buyer <span class="helvetica-light-italic">Personas</span></h2>
          <IconCardSubtitle
            v-for="(item, index) in section_two"
            :key="index"
            :info="item" />
        </div>
        <div class="timeline-printa" id="timeline-center">
          <div class="third">
            <div class="line" />
            <span class="step">3.0</span>
            <div class="circle circle-white-black" />
            <span class="title" id="title1">Ideate</span>
          </div>
          <div class="third">
            <span class="step">2.0</span>
            <div class="line" />
            <div class="circle circle-black" />
            <span class="title" id="title1">Define</span>
          </div>
          <div class="third">
            <span class="step">1.0</span>
            <div class="line" />
            <div class="circle circle-white-stripes" />
            <span class="title" id="title1">Empathize</span>
          </div>
        </div>
        <div class="cont80 text-center logo-symbol">
          <h2>Buyer <span class="helvetica-light-italic">Personas</span></h2>
          <p class="subtitle">Significado</p>
          <p class="summary">Printa delivery es una empresa dedicada a la impresión y corte láser de obras y trabajos de arquitectos y diseñadores. es entonces necesario que el logo identifique a ambas profesiones, su constante búsqueda por la sencillez estética y su carga en significado. El logosímbolo describe un ejercicio tipográfico usando una fuente icónica y de fácil recordación, la helvetica; el achurado en diagonal hace un gesto al dibujo descriptivo mientras, las guías de corte enmarcan los ámbitos del corte y la impresión.</p>
          <p class="subtitle">Construcción</p>
          <p class="summary">Para la construcción del logotipo se crea una retícula de las medidas y proporciones exactas de cada uno de los elementos que componen la imagen corporativa. Se estudia la forma en búsqueda de lograr una alta legibilidad del logo, espaciando cuidadosamente la tipografía y manteniendo la distancia entre cada elemento.</p>
          <p class="subtitle">Area de Respeto</p>
          <p class="">Para mantener el logo limpio y lograr un mayor impacto visual se deben mantener siempre unas distancias libres de textos o cualquier elemento gráfico igual a 4x para borde superior e inferior y 3x para bordes laterales.</p>
          <p class="summary">*(x = altura de letra de “Printadelivery”)</p>
          <img src="~/static/img/printa/printa-logo.png" alt="">
        </div>
        <div class="timeline-printa margin-bottom">
          <div class="third">
            <div class="line" />
            <span class="step">2.0</span>
            <div class="circle circle-white-stripes" />
            <span class="title" id="title1">Define</span>
          </div>
          <div class="third">
            <span class="step">3.0</span>
            <div class="line" />
            <div class="circle circle-black" />
            <span class="title" id="title1">Ideate</span>
          </div>
          <div class="third">
            <span class="step">4.0</span>
            <div class="line" />
            <div class="circle circle-white-black" />
            <span class="title" id="title1">Prototype</span>
          </div>
        </div>
        <div class="ideate">
          <img src="~/static/img/printa/ideate-background.png" alt="">
          <div class="cont80 text-center">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
        </div>
        <div class="timeline-printa margin-bottom">
          <div class="third">
            <div class="line" />
            <span class="step">5.0</span>
            <div class="circle circle-white-black" />
            <span class="title" id="title1">Test</span>
          </div>
          <div class="third">
            <span class="step">4.0</span>
            <div class="line" />
            <div class="circle circle-black" />
            <span class="title" id="title1">Prototype</span>
          </div>
          <div class="third">
            <span class="step">3.0</span>
            <div class="line" />
            <div class="circle circle-white-stripes" />
            <span class="title" id="title1">Ideate</span>
          </div>
        </div>
        <div class="prototype margin-bottom">
          <img src="~/static/img/printa/prototype.png" alt="Prototype">
        </div>
        <div class="timeline-printa margin-bottom">
          <div class="third">
            <div class="line" />
            <span class="step">4.0</span>
            <div class="circle circle-white-black" />
            <span class="title" id="title1">Prototype</span>
          </div>
          <div class="third">
            <span class="step">5.0</span>
            <div class="line" />
            <div class="circle circle-black" />
            <span class="title" id="title1">Test</span>
          </div>
          <div class="third">
            <span class="step">6.0</span>
            <div class="line" />
            <div class="circle circle-white-stripes" />
            <span class="title" id="title1">Implement</span>
          </div>
        </div>
        <div class="test margin-bottom">
          <img src="~/static/img/printa/test.png" alt="Test">
        </div>
        <div class="timeline-printa margin-bottom">
          <div class="third">
            <span class="step">6.0</span>
            <div class="line" />
            <div class="circle circle-black" />
            <span class="title" id="title1">Implement</span>
          </div>
          <div class="third">
            <span class="step">5.0</span>
            <div class="line" />
            <div class="circle circle-whitez-stripes" />
            <span class="title" id="title1">Test</span>
          </div>
        </div>
        <div class="implement">
          <img src="~/static/img/printa/implement.png" alt="Implement">
        </div>
        <div class="branding">
          <div class="cont80">
            <div class="font-row first">
              <div class="font-row-left">
                <p class="helvetica-light-bold">Printa</p>
              </div>
              <div class="font-row-right">
                <p class="helvetica-light-bold">Helvetica Neue Bold</p>
              </div>
            </div>
            <div class="font-row second">
              <div class="font-row-left">
                <p class="helvetica-light-italic">Delivery</p>
              </div>
              <div class="font-row-right">
                <p class="helvetica-light-italic">Helvetica Neue Light Oblique</p>
              </div>
            </div>
            <div class="font-row third margin-bottom">
              <div class="font-row-left">
                <p class="avenir">Tus entregas</p>
              </div>
              <div class="font-row-right">
                <p class="avenir">Avenir LT Std</p>
              </div>
            </div>
            <ColorPalette :colors="colors" class="margin-bottom" />
            <div class="cards">
              <img src="~/static/img/printa/card1.png" class="card" alt="Card Printa">
              <img src="~/static/img/printa/card2.png" class="card margin-bottom-small" alt="Card Printa">
              <img src="~/static/img/printa/card3.png" class="card" alt="Card Printa">
              <img src="~/static/img/printa/card4.png" class="card margin-bottom" alt="Card Printa">
            </div>
          </div>
          <div class="finished text-center">
            <div class="cont80">
              <h2>Finished <span class="helvetica-light-italic">Product</span></h2>
              <img src="~/static/img/printa/logowhite.png" alt="">
              <p>Este manual de identidad corporativa es una guía de referencia que contiene las normas básicas indispensables para el uso correcto de los distintos elementos gráficos que conforman Printa delivery.</p>
            </div>
          </div>
        </div>
      </section>

    </main>

  </div>
</template>

<script>
import data from '~/assets/data/printa.json'
import IconCard from '~/components/CaseStudies/Printa/IconCard.vue'
import IconCardSubtitle from '~/components/CaseStudies/Printa/IconCardSubtitle.vue'
import ColorPalette from '~/components/CaseStudies/Printa/ColorPalette.vue'

export default {
  data() {
    return {
      section_one: data.section_one,
      section_two: data.section_two,
      colors: data.colors
    }
  },
  components: {
    IconCard,
    IconCardSubtitle,
    ColorPalette
  }
}
</script>

<style lang="scss">
@import '~/assets/fonts/printafonts/style.css';
@import '~/assets/css/helpers/_mixins.scss';

// Variables
$helvetica-light: 'Helvetica Neue LT Std', helvetica, sans-serif;
$helvetica-light-italic: 'Helvetica Neue LT Std Italic', helvetica, sans-serif;
$helvetica-light-bold: 'Helvetica Neue LT Std Bold', helvetica, sans-serif;
$avenir: 'Avenir LT Std', helvetica, sans-serif;

$color-blue: #00a9ea;
$color-red: #ee4066;
$color-yellow: #ffc34a;

// GLOBAL STYLES
body {
  background-image: url('~/static/img/printa-background.png');
  background-position: center;
  font-family: $avenir;
}

h1, h2, h3, h4, h5, h6 {
  font-family: $helvetica-light-bold;
  font-weight: normal;
}

p {
  color: #808080;
}

.helvetica-light {
  font-family: $helvetica-light;
}
.helvetica-light-italic {
  font-family: $helvetica-light-italic;
}
.helvetica-light-bold {
  font-family: $helvetica-light-bold;
}
.avenir {
  font-family: $avenir;
}

.image-title {
  width: 200px;
  height: auto;
  margin: auto;
}

.section-title {
  margin-bottom: 70px;
}

.double-border {
  border-top: 1px solid #b3b3b3;
  border-bottom: 1px solid #b3b3b3;
}

.color-blue {
  color: $color-blue;
}
.color-red {
  color: $color-red;
}
.color-yellow {
  color: $color-yellow;
}

.margin-bottom {
  margin-bottom: 30px;
}

// SECTIONS
#section-first-fold {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
  height: 750px;
  margin-bottom: 80px;
  .first-fold-container {
    width: 80%;
    max-width: 450px;
    text-align: center;
    img {
      width: 200px;
      height: auto;
    }
    h1 {
      margin: 40px 0;
    }
  }
}

#section-one {
  margin-bottom: 120px;
  .icons-container {
    margin-bottom: 70px;
  }
  .messages-cont {
    .titles {
      font-size: 24px;
      font-family: $helvetica-light-bold;
      margin: 14px 0;
      display: block;
    }
    .message {
      color: #808080;
      margin-top: 40px;
    }
  }
}

#section-two {
  .timeline-printa {
    display: flex;
    .half,
    .third {
      flex: 1;
      position: relative;
      .line {
        display: block;
        position: absolute;
        top: 51px;
        width: 100%;
        height: 2px;
        background-color: #000;
        z-index: -1;
      }
      .circle {
        display: inline-block;
        width: 32px;
        height: 32px;
        z-index: 3;
        @include border-radius(50%);
      }
      .circle-black {
        background-color: #000;
        border: 3px solid #000;
      }
      .circle-white-black {
        background-color: #fff;
        border: 3px solid #000;
      }
      .circle-white-stripes {
        background-image: url('~/static/img/printa/circle.png');
        background-size: cover;
        border: 3px solid #000;
      }
      .step {
        display: block;
        font-family: $helvetica-light-bold;
        position: relative;
        margin-bottom: 15px;
        font-size: 14px;
      }
      .title {
        display: block;
        font-family: $helvetica-light-bold;
        margin-top: 15px;
        font-size: 14px;
      }
    }
    .half {

    }
    .third {
      text-align: center;
      .circle {
        left: 0;
      }
    }
  }
  .margin-bottom {
    margin-bottom: 70px;
  }
  .margin-bottom-small {
    margin-bottom: 50px;
  }
  #timeline-above {
    margin-bottom: 70px;
    text-align: center;
  }
  #timeline-center {
    margin-bottom: 70px;
  }
  .logo-symbol {
    margin-bottom: 70px;
    h2 {
      margin-bottom: 50px;
    }
    .subtitle {
      font-family: $helvetica-light-bold;
      color: #000;
    }
    .summary {
      margin-bottom: 40px;
    }
  }
  .ideate {
    margin-bottom: 70px;
    img {
      margin-bottom: 30px;
    }
  }
  .manifesto {
    background-color: #000;
    h2 {
      color: #fff;
    }
  }
  .implement {
    margin-bottom: 70px;
  }
  .branding {
    .font-row {
      display: flex;
      .font-row-left {
        flex: 2;
      }
      .font-row-right {
        flex: 3;
      }
    }
    .first {
      font-size: 24px;
    }
    .second {
      font-size: 20px;
    }
    .finished {
      background-color: #000;
      padding: 50px 0;
      h2 {
        color: #fff;
      }
      img {
        width: 180px;
        margin: 15px 0;
      }
      p {
        color: #fff;
      }
    }
  }
}
</style>
