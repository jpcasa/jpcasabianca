<template lang="html">
  <div id="main-printa">

    <nuxt-link class="icon-arrow-left" id="back" to="/case-studies"></nuxt-link>

    <!-- MAIN SECTION -->
    <main>

      <!-- SECTION #1 -->
      <section id="section-first-fold-printa">
        <div class="first-fold-container">
          <img src="~/static/img/printa-delivery.png" alt="Printa Delivery">
          <h1>Ctrl+P = <span class="helvetica-light-italic">“The Biggest Headache Ever”</span></h1>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
      </section>

      <!-- SECTION #1 -->
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

      <!-- SECTION #2 -->
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
          <div class="buyer-persona-cards">
            <IconCardSubtitle
              v-for="(item, index) in section_two"
              :key="index"
              :info="item" />
          </div>
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
          <h2>Ctrl + P <span class="helvetica-light-italic">== Easy</span></h2>
          <div class="logo-symbol-cont">
            <div class="logo-symbol-info">
              <p class="subtitle">Significado</p>
              <p class="summary">Printa delivery es una empresa dedicada a la impresión y corte láser de obras y trabajos de arquitectos y diseñadores. es entonces necesario que el logo identifique a ambas profesiones, su constante búsqueda por la sencillez estética y su carga en significado. El logosímbolo describe un ejercicio tipográfico usando una fuente icónica y de fácil recordación, la helvetica; el achurado en diagonal hace un gesto al dibujo descriptivo mientras, las guías de corte enmarcan los ámbitos del corte y la impresión.</p>
              <p class="subtitle">Construcción</p>
              <p class="summary">Para la construcción del logotipo se crea una retícula de las medidas y proporciones exactas de cada uno de los elementos que componen la imagen corporativa. Se estudia la forma en búsqueda de lograr una alta legibilidad del logo, espaciando cuidadosamente la tipografía y manteniendo la distancia entre cada elemento.</p>
              <p class="subtitle">Area de Respeto</p>
              <p class="">Para mantener el logo limpio y lograr un mayor impacto visual se deben mantener siempre unas distancias libres de textos o cualquier elemento gráfico igual a 4x para borde superior e inferior y 3x para bordes laterales.</p>
              <p class="summary">*(x = altura de letra de “Printadelivery”)</p>
            </div>
            <div class="logo-symbol-img">
              <img src="~/static/img/printa/printa-logo.png" alt="">
            </div>
          </div>
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
          <img src="~/static/img/printa/ideate-background.png" class="printa-mobile" alt="">
          <img src="~/static/img/printa/ideate-background-desktop.png" class="printa-desktop" alt="">
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
          <img src="~/static/img/printa/prototype.png" class="printa-mobile" alt="Prototype">
          <img src="~/static/img/printa/prototype-desktop.png" class="printa-desktop" alt="Prototype">
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
          <img src="~/static/img/printa/test.png" class="printa-mobile" alt="Test">
          <img src="~/static/img/printa/test-desktop.png" class="printa-desktop" alt="Test">
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
          <img src="~/static/img/printa/implement.png" class="printa-mobile" alt="Implement">
          <img src="~/static/img/printa/implement-desktop.png" class="printa-desktop" alt="Implement">
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

      <!-- SECTION #3 -->
      <section id="section-three">
        <div class="cont80 text-center">
          <img src="~/static/img/printa/3.png" alt="" class="image-title">
          <h2 class="section-title">Happy <span class="helvetica-light-italic">Coding</span></h2>
          <p class="copy">Me irresponsible? All I wanted was for you to hand me a screwdriver! But instead you had me buckle down and make you a roofie juice serum, so you can roofie that poor girl at your school. W-w-w-w--are you kidding me, Morty?! You're really gonna try to take the high road on this one? Y'know your-you're a little creep, Morty! Your-your-your-you're just a little creepy creep person!</p>
          <div class="font-row first">
            <div class="font-row-left">
              <p class="helvetica-light-bold color-red">Challenge 1</p>
            </div>
            <div class="font-row-right">
              <p class="helvetica-light-bold">Endless Printing Options</p>
            </div>
          </div>
          <div class="font-row second">
            <div class="font-row-left">
              <p class="helvetica-light-italic color-blue">Challenge 2</p>
            </div>
            <div class="font-row-right">
              <p class="helvetica-light-italic">The Application State</p>
            </div>
          </div>
          <div class="font-row third margin-bottom-big">
            <div class="font-row-left">
              <p class="avenir color-yellow">Challenge 3</p>
            </div>
            <div class="font-row-right">
              <p class="avenir">Live order tracking for client and product manager</p>
            </div>
          </div>
          <div class="solution-1 margin-bottom-big">
            <h2 class="margin-bottom color-red">Solution 1</h2>
            <p class="margin-bottom-normal">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <img src="~/static/img/printa/chars1.png" alt="Characteristics 1" class="margin-bottom">
            <img src="~/static/img/printa/chars2.png" alt="Characteristics 2">
          </div>
          <div class="solution-2">
            <h2 class="margin-bottom color-blue">Solution 2</h2>
            <p class="margin-bottom-normal">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
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
        <img src="~/static/img/printa/doubts.png" alt="Doubts" class="margin-bottom-big">
        <div class="cont80 solution-3 text-center margin-bottom">
          <h2 class="color-yellow">Solution 3</h2>
          <h3 class="helvetica-light-italic">Live Tracking for the complicated process</h3>
          <p>Do you know how many characters there are in the Simpsons Morty? There's like a-a billion characters, M-Morty. There was an episode where Former President BUSH was their neighbor!</p>
        </div>
        <img src="~/static/img/printa/solution-3.png" alt="Solution 3" class="margin-bottom-big printa-mobile">
        <img src="~/static/img/printa/solution-3-desktop.png" alt="Solution 3" class="margin-bottom-big printa-desktop">
        <div class="cont80 developing text-center">
          <h2 class="section-title">Too Much <span class="helvetica-light-italic">User Interaction</span></h2>
          <p class="margin-bottom-big">Me irresponsible? All I wanted was for you to hand me a screwdriver! But instead you had me buckle down and make you a roofie juice serum, so you can roofie that poor girl at your school. W-w-w-w--are you kidding me, Morty?! You're really gonna try to take the high road on this one? Y'know your-you're a little creep, Morty! Your-your-your-you're just a little creepy creep person!</p>
          <h2 class="section-title">Bring on <span class="helvetica-light-italic">The Muscle</span></h2>
          <img src="~/static/img/printa/coding.png" alt="Coding" class="margin-bottom printa-mobile">
          <img src="~/static/img/printa/coding-desktop.png" alt="Coding" class="margin-bottom printa-desktop">
          <p>Wow, so your origin is what? You fell into a vat of redundancy?</p>
        </div>
      </section>

      <!-- SECTION #4 -->
      <section id="section-four">
        <div class="text-center cont80">
          <img src="~/static/img/printa/4.png" alt="" class="image-title">
          <h2 class="section-title">Testing <span class="helvetica-light-italic">The Platform</span></h2>
          <div class="icons-container">
            <IconCard
              v-for="(item, index) in section_four"
              :key="index"
              :info="item" />
          </div>
        </div>
        <img src="~/static/img/printa/bugs.png" class="printa-mobile" alt="bugs">
        <img src="~/static/img/printa/bugs-desktop.png" class="printa-desktop" alt="bugs">
        <h3 class="text-center black-bug">A Couple <span class="helvetica-light-italic">Bugs Later...</span></h3>
        <img src="~/static/img/printa/home.png" alt="Home">
        <img src="~/static/img/printa/home2.png" alt="Home">
      </section>

      <!-- SECTION #5-6 -->
      <section id="section-five-six">
        <div class="text-center cont80">
          <img src="~/static/img/printa/56.png" alt="" class="image-title">
          <h2 class="section-title">Inbound <span class="helvetica-light-italic">Marketing</span></h2>
          <img src="~/static/img/printa/inbound.png" alt="Inbound Marketing" class="margin-bottom printa-mobile">
          <img src="~/static/img/printa/inbound-desktop.png" alt="Inbound Marketing" class="margin-bottom printa-desktop">
          <p class="margin-bottom-big">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          <h2>Digital <span class="helvetica-light-italic">Samples</span></h2>
          <div class="samples-container">
            <img src="~/static/img/printa/sample1.png" alt="Sample Inbound Marketing">
            <img src="~/static/img/printa/sample2.png" alt="Sample Inbound Marketing">
            <img src="~/static/img/printa/sample3.png" alt="Sample Inbound Marketing">
            <img src="~/static/img/printa/sample4.png" alt="Sample Inbound Marketing">
          </div>
        </div>
      </section>

      <!-- SECTION #7 -->
      <section id="section-seven">
        <div class="text-center cont80 margin-bottom-normal">
          <img src="~/static/img/printa/7.png" alt="" class="image-title">
          <h2 class="margin-bottom">Show Me <span class="helvetica-light-italic">The Numbers</span></h2>
          <p>Wow I really crononberg'd up the whole place huh Morty, just a bunch a cronenbergs walkin around.</p>
        </div>
        <div class="timeline-printa margin-bottom-big">
          <div class="third">
            <div class="line" />
            <span class="step">1.0</span>
            <div class="circle circle-white-black" />
            <span class="title" id="title1">Acquire</span>
          </div>
          <div class="third">
            <span class="step">2.0</span>
            <div class="line" />
            <div class="circle circle-black" />
            <span class="title" id="title1">Retain</span>
          </div>
          <div class="third">
            <span class="step">3.0</span>
            <div class="line" />
            <div class="circle circle-white-stripes" />
            <span class="title" id="title1">Monetize</span>
          </div>
        </div>
        <div class="cont80 text-center">
          <div class="kpis">
            <div class="kpi">
              <h3 class="margin-bottom">Unique <span class="helvetica-light-italic">Visitors</span></h3>
              <p>Like nothing shady ever happened in a fully furnished office? You ever hear about Wall Street Morty? You know what those guys do in their fancy board rooms? They take their balls and dip 'em in cocaine and wipe 'em all over each other. You know Grandpa goes around and he does his business in public because grandpa isn't shady.</p>
            </div>
            <div class="kpi">
              <h3 class="margin-bottom">Leads to <span class="helvetica-light-italic">Customer</span></h3>
              <p>Like nothing shady ever happened in a fully furnished office? You ever hear about Wall Street Morty? You know what those guys do in their fancy board rooms? They take their balls and dip 'em in cocaine and wipe 'em all over each other. You know Grandpa goes around and he does his business in public because grandpa isn't shady.</p>
            </div>
          </div>
        </div>
        <img src="~/static/img/printa/kpis.png" alt="KPIs" class="printa-mobile">
        <img src="~/static/img/printa/kpis-desktop.png" alt="KPIs" class="printa-desktop margin-bottom-normal">
      </section>

      <!-- SECTION #8 -->
      <section id="section-eight">
        <div class="text-center cont80 margin-bottom-normal">
          <img src="~/static/img/printa/8.png" alt="" class="image-title">
          <h2 class="margin-bottom">Optimization <span class="helvetica-light-italic">Time</span></h2>
          <p class="margin-bottom-normal">Wow I really crononberg'd up the whole place huh Morty, just a bunch a cronenbergs walkin around.z</p>
          <img src="~/static/img/printa/optimization.png" alt="Optimization" class="margin-bottom printa-mobile">
          <img src="~/static/img/printa/optimization-desktop.png" alt="Optimization" class="margin-bottom printa-desktop">
          <p>You're not gonna believe this, because it usually never happens, but I made a mistake.</p>
        </div>
      </section>

      <!-- SECTION #9 -->
      <section id="section-nine">
        <div class="text-center cont80">
          <img src="~/static/img/printa/9.png" alt="" class="image-title">
          <h2 class="margin-bottom">Immediate <span class="helvetica-light-italic">Sales Contact</span></h2>
          <p class="margin-bottom-normal">Wow I really crononberg'd up the whole place huh Morty, just a bunch a cronenbergs walkin around.z</p>
        </div>
        <img src="~/static/img/printa/sales.png" alt="Sales" class="printa-mobile">
        <img src="~/static/img/printa/sales-desktop.png" alt="Sales" class="printa-desktop">
      </section>

      <!-- SECTION #10 -->
      <section id="section-ten">
        <div class="text-center cont80">
          <h2 class="margin-bottom">Liked what <span class="helvetica-light-italic">you saw?</span></h2>
          <p class="margin-bottom">It's like the N word and the C word had a baby, and it was raised by all the bad words for Jews.</p>
          <nav class="info">
            <a href="tel:+573507015800" class="back-hover-blue"><i class="icon-phone" />Call Me</a>
            <a href="mailto:hola@jpcasabianca.com" class="back-hover-red"><i class="icon-mail" />Email Me</a>
            <a href="https://wa.me/573507015800" class="back-hover-yellow"><i class="icon-message-circle" />Whatsapp</a>
          </nav>
        </div>
      </section>

    </main>
    <!-- END MAIN SECTION -->

    <!-- INFO NAV -->
    <nav id="info-nav">
      <a class="back-hover-blue" href="tel:+573507015800">
        <i class="icon-phone" />
        <span>Call Me</span>
      </a>
      <a class="back-hover-red" href="mailto:hola@jpcasabianca.com">
        <i class="icon-mail" />
        <span>Email Me</span>
      </a>
      <a class="back-hover-yellow" href="https://wa.me/573507015800">
        <i class="icon-message-circle" />
        <span>Whatsapp</span>
      </a>
    </nav>

  </div>
</template>

<script>
import data from '~/assets/data/printa.json'
import LineChart from '~/components/Elements/Charts/LineChart.js'

import IconCard from '~/components/CaseStudies/Printa/IconCard.vue'
import IconCardSubtitle from '~/components/CaseStudies/Printa/IconCardSubtitle.vue'
import ColorPalette from '~/components/CaseStudies/Printa/ColorPalette.vue'

export default {
  layout: 'case-study',
  data() {
    return {
      section_one: data.section_one,
      section_two: data.section_two,
      colors: data.colors,
      section_four: data.section_four,
      chartData: {
        labels: ['Running', 'Swimming', 'Eating'],
        datasets: [{
          data: [3, 7, 9],
          backgroundColor: 'rgba(62, 236, 130, 0.5)',
          borderColor: '#23c286',
        }]
      }
    }
  },
  components: {
    IconCard,
    IconCardSubtitle,
    ColorPalette,
    LineChart
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
#main-printa {
  background-image: url('~/static/img/printa-background.png')!important;
  background-color: #fff;
  background-position: center;
  font-family: $avenir;
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
  .margin-bottom-big {
    margin-bottom: 70px;
  }
  .margin-bottom-normal {
    margin-bottom: 50px;
  }

  .printa-desktop,
  .printa-desktop-flex,
  .printa-desktop-inline {
    display: none;
  }
}


// SECTIONS
#back {
  position: fixed;
  left: 15px;
  top: 15px;
  background-color: #000;
  color: #fff;
  padding: 6px 6px 7px 7px;
  font-size: 24px;
  z-index: 999;
  text-decoration: none;
  @include border-radius(50%);
  @include animation(colors 10s infinite);
}

@keyframes colors {
    0% {background-color: #000;}
    25% {background-color: $color-red;}
    50% {background-color: $color-blue;}
    75% {background-color: $color-yellow;}
    100% {background-color: #000;}
}

#info-nav {
  position: fixed;
  width: 100%;
  bottom: 0;
  left: 0;
  display: flex;
  text-align: center;
  a {
    flex: 1;
    text-decoration: none;
    background-color: #000;
    padding: 5px 0;
    i, span {
      display: block;
      color: #fff;
    }
    span {
      font-size: 13px;
    }
    i {
      margin-bottom: 4px;
    }
  }
  .back-hover-blue {
    &:hover {
      background-color: $color-blue;
    }
  }
  .back-hover-red {
    &:hover {
      background-color: $color-red;
    }
  }
  .back-hover-yellow {
    &:hover {
      background-color: $color-yellow;
    }
  }
}

#section-first-fold-printa {
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
  margin-bottom: 70px;
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
      font-size: 15px;
    }
    .summary {
      margin-bottom: 20px;
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

.font-row {
  display: flex;
  text-align: left;
  .font-row-left {
    flex: 2;
  }
  .font-row-right {
    flex: 3;
  }
}

.font-row.first {
  font-size: 20px;
}

.font-row.second {
  font-size: 18px;
}

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

#section-three {
  margin-bottom: 70px;
  .copy {
    margin-bottom: 50px;
  }
  .developing {
    h2 {
      margin-bottom: 30px;
    }
  }
}

#section-four {
  margin-bottom: 70px;
  .black-bug {
    background-color: #000;
    margin: 0;
    color: #fff;
    padding: 50px 0;
    margin-top: -5px;
  }
}

#section-five-six {
  margin-bottom: 70px;
  .samples-container {
    img {
      margin-bottom: 25px;
    }
  }
}

#section-seven {
  .kpis {
    .kpi {
      margin-bottom: 50px;
    }
  }
}

#section-eight {
  margin-bottom: 70px;
}

#section-nine {
  margin-bottom: 70px;
}

#section-ten {
  margin-bottom: 70px;
  .info {
    a {
      display: inline-block;
      text-decoration: none;
      color: #fff;
      background-color: #000;
      padding: 10px 20px;
      margin: 0 5px 15px 5px;
      i {
        display: inline-block;
        margin-right: 4px;
      }
    }
    .back-hover-blue {
      &:hover {
        background-color: $color-blue;
      }
    }
    .back-hover-red {
      &:hover {
        background-color: $color-red;
      }
    }
    .back-hover-yellow {
      &:hover {
        background-color: $color-yellow;
      }
    }
  }
}

@media (min-width: 800px) {

  .printa-mobile {
    display: none;
  }

  .printa-desktop {
    display: block;
  }

  .printa-desktop-inline {
    display: inline-block;
  }

  .printa-desktop-flex {
    display: flex;
  }

  .icons-container {
    display: flex;
    .printa-icon-card {
      flex: 1;
      margin: 0 12px;
    }
  }

  .buyer-persona-cards {
    display: flex;
    margin-bottom: 70px;t
    .printa-icon-card {
      flex: 1;
      margin: 0 12px;
    }
  }

  .logo-symbol-cont {
    display: flex;
    .logo-symbol-info {
      flex: 2;
      text-align: left;
      margin-right: 40px;
      .summary {
        font-size: 14px;
      }
    }
    .logo-symbol-img {
      flex: 2;
    }
  }

  .cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    .card {
      width: 300px;
      margin: 0 10px;
      height: 180px;
    }
  }

  .samples-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    img {
      width: 280px;
      margin: 0 10px 25px 10px;
    }
  }

  .kpis {
    display: flex;
    .kpi {
      flex: 1;
      margin: 0 25px;
    }
  }

}

@media (min-width: 1200px) {

  .icons-container {
    .printa-icon-card {
      margin: 0 25px;
    }
  }
  .buyer-persona-cards {
    .printa-icon-card {
      margin: 0 25px;
    }
  }
}
</style>
