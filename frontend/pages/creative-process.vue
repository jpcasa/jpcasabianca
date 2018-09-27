<template>
  <section>

    <section id="digital-world">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-digital"
          class="text-center"
          title="The Digital World is Complex"
          subtitle="How my brain works..."
          copy="With an ever-changing digital world, having a creative process can help get sh*t done. Everything is intangible, so it’s up to us to try to make everything as tangible and understanding as possible."
          theme="light" />
        <img src="img/design-thinking.png" alt="Design Thinking" class="image-responsive">
      </div>
    </section>

    <section id="design-thinking">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-design-patterns"
          class="text-center"
          title="Design Thinking"
          subtitle="My approach to problem solving"
          copy='Design thinking is a fantastic way to solve complex problems. For those of you not familiar with Design Thinking you can read more about it <a href="https://www.ideou.com/pages/design-thinking" target="_blank">here</a>. With design thinking you can come up with a great solution to a complex problem.'
          theme="light" />
        <img src="img/ui-ux.png" alt="UI / UX Patterns" id="ui-image" class="image-responsive">
        <TabsFullSimple styles="light" :items="design_thinking_steps" />
      </div>
    </section>

    <section id="ui-ux-patterns">
      <div class="container text-center">
        <img src="img/scrum-img.png" alt="Scrum" class="image-responsive">
        <SimpleTitle
          id="simple-title-ui-ux"
          class="text-center"
          title="UI / UX Patterns"
          subtitle="Very handful tools"
          copy="Although design thinking is great, we really don’t have to reinvent the wheel. There are a lot of useful and cool design patterns that I normally use for my work. Check some out."
          theme="light" />
        <TabsFullCards :items="design_patterns" />
      </div>
    </section>

    <section id="agile-scrum">
      <div class="container">
        <SimpleTitle
          id="simple-title-scrum"
          class="text-center"
          title="Agile - Scrum"
          subtitle="When it comes to coding"
          copy="Agile is a cool methodology used by a lot of dev teams all over the world. If you haven’t heard of it I really recommend checking out this video, if you have, then you’re totally picturing the Post It’s on the task board right now."
          theme="light" />
        <IconSection :items="agile_section" />
      </div>
      <img src="img/scrum-agile.png" alt="Scrum Agile" class="mobile">
      <img src="img/scrum-agile-desktop.png" alt="Scrum Agile" class="desktop">
    </section>

    <section id="inbound-marketing">
      <div class="container">
        <SimpleTitle
          id="simple-title-inbound"
          class="text-center"
          title="Inbound Marketing"
          subtitle="Understanding the customer"
          copy='Every designer and developer should learn about inbound marketing to really understand the client. If you don’t know what inbound marketing is read <a target="_blank" href="https://medium.com/@jpc_774/the-difference-between-outbound-and-inbound-marketing-fda4ee7a2e91">my medium article (2 min read)</a> about it. With inbound in mind, you can help the marketing team optimize product performance, stats, and analysis. Cool, right?'
          theme="light" />
      </div>
      <div class="text-center">
        <img src="img/inbound2.png" id="inbound-marketing-img" alt="Inbound Marketing" class="image-responsive">
      </div>
    </section>

    <section id="automation">
      <div class="container">
        <SimpleTitle
          id="simple-title-automation"
          class="text-center"
          title="Automation"
          subtitle="The art of delegation"
          copy="A key thing of my creative process is to automate simple tasks so I can focus on the things that create the most value. If you want to check out some programs to automate processes go here."
          theme="light" />
      </div>
      <img src="img/automation.png" alt="Automation" class="mobile">
      <img src="img/automation-desktop.png" alt="Automation" class="desktop">
    </section>

    <section id="data-analysis">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-automation"
          class="text-center"
          title="Data Analysis"
          subtitle="Coming Soon"
          copy='Since I finished my business major, I’ve always had a passion for data. You can check out <a href="#" target="_blank">my paper on financial analysis on family companies in Colombia</a>. I already learned Inbound Marketing to generate more data, now I want to take it up a notch and not only generate data but understand and interpret it. Coming Soon!'
          theme="dark" />
        <img src="img/data-analysis.png" alt="Data Analysis" class="image-responsive">
      </div>
    </section>

  </section>
</template>

<script>
import SimpleTitle from '~/components/Elements/Titles/SimpleTitle.vue'
import TabsFullSimple from '~/components/Navigation/Tabs/TabsFullSimple.vue'
import TabsFullCards from '~/components/Navigation/Tabs/TabsFullCards.vue'
import IconSection from '~/components/Sections/IconSection.vue'
import InboundSection from '~/components/Sections/InboundSection.vue'

export default {
  data() {
    return {
      design_thinking_steps: [
        {
          'id': 0,
          'title': '1.<br>Empathize',
          'img': 'img/empathize.svg',
          'copy': '<span class="color-green">Empathy</span> is the key for life, because it’s the path to understanding. Putting yourself in people’s shoes can really make you understand what’s going through their minds.'
        },
        {
          'id': 1,
          'title': '2.<br>Define',
          'img': 'img/define.svg',
          'copy': 'After really understanding the problem, you must <span class="color-green">define</span> the best approach to solving it. You declare personas (people that will use your product or service), what’s going to be easy, what challenges you face, decision to make, etc...'
        },
        {
          'id': 2,
          'title': '3.<br>Ideate',
          'img': 'img/ideate.svg',
          'copy': 'When you define something clearly enough, you can start <span class="color-green">ideating</span> the best solution. This is an analysis stage where you or the team prioritizes work. You come in stronger to a match if you have a game plan.'
        },
        {
          'id': 3,
          'title': '4.<br>Prototype',
          'img': 'img/prototype.svg',
          'copy': 'With the game plan and solution laid out, you can create a real tangible <span class="color-green">prototype</span> of the solution. '
        },
        {
          'id': 4,
          'title': '5.<br>Test',
          'img': 'img/test.svg',
          'copy': 'Finally, with a solution in your hands you can start <span class="color-green">testing</span> it. Iterate quickly, understand what works and create a roadmap to improve the solution.'
        }
      ],
      design_patterns: [
        {
          'id': 0,
          'title': '1.<br>UI Patterns',
          'img': 'img/uipatterns.svg',
          'cards': [
            {
              'icon': 'img/icon-forms.svg',
              'title': 'Inputs & Forms'
            },
            {
              'icon': 'img/icon-navigation.svg',
              'title': 'Navigation'
            },
            {
              'icon': 'img/icon-data.svg',
              'title': 'Data'
            },
            {
              'icon': 'img/icon-shopping.svg',
              'title': 'Shopping'
            },
            {
              'icon': 'img/icon-social.svg',
              'title': 'Social'
            },
            {
              'icon': 'img/icon-onboarding.svg',
              'title': 'Onboarding'
            }
          ]
        },
        {
          'id': 1,
          'title': '2.<br>Behavioral Patterns',
          'img': 'img/behaviorpatterns.svg',
          'cards': [
            {
              'icon': 'img/icon-recognition-over-recall.svg',
              'title': 'Recognition over recall'
            },
            {
              'icon': 'img/icon-gamification.svg',
              'title': 'Gamification'
            },
            {
              'icon': 'img/icon-cognition.svg',
              'title': 'Cognition'
            },
            {
              'icon': 'img/icon-feedback.svg',
              'title': 'Feedback'
            },
            {
              'icon': 'img/icon-social.svg',
              'title': 'Social'
            }
          ]
        }
      ],
      agile_section: [
        {
          'icon': 'img/product-owner.svg',
          'title': 'Product Owner',
          'subtitle': 'David',
          'list': ['Handles Communication with the customer', 'Prioritizes Backlog', 'Communicates with dev team']
        },
        {
          'icon': 'img/scrum-master.svg',
          'title': 'Scrum Master',
          'subtitle': 'Sara',
          'list': ['Helps Team Deliver', 'Identifies Hassles', 'Princess Leia (total badass)']
        },
        {
          'icon': 'img/dev-team.svg',
          'title': 'Dev Team Members',
          'subtitle': 'Kim, Andy, Jane',
          'list': ['Deliver a really good product', 'Order a bunch of food', 'Write awesome code']
        }
      ]
    }
  },
  components: {
    SimpleTitle,
    TabsFullSimple,
    TabsFullCards,
    IconSection,
    InboundSection
  }
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';

#digital-world {
  background-color: $color-gray-light;
  #simple-title-digital {
    padding-top: 70px;
    .subtitle {
      margin: 0 0 8px 0;
    }
  }
}

#design-thinking {
  background-image: url('~/static/img/ui-patterns.png');
  background-size: cover;
  padding: 160px 0 40px 0;
  #simple-title-design-patterns {
    .subtitle {
      margin: 0 0 8px 0;
    }
  }
  #ui-image {
    margin-bottom: 30px;
  }
}

#ui-ux-patterns {
  background-image: url('~/static/img/scrum.png');
  background-size: cover;
  #simple-title-ui-ux {
    margin-bottom: 40px;
  }
}

#agile-scrum {
  padding-top: 50px;
  .lower-scrum {
    margin-top: -5px;
    padding: 60px 0 180px 0;
    background-image: url('~/static/img/lower-scrum.png');
    background-size: cover;
    background-position: bottom;
  }
}

#inbound-marketing {
  #inbound-marketing-img {
    margin-bottom: 30px;
  }
}

#data-analysis {
  background-color: $color-blue;
  margin-top: -5px;
  padding: 50px 0 0 0;
  .subtitle {
    margin: 0;
  }
}

@media (min-width: 768px) {
  #design-thinking {
    padding: 250px 0 40px 0;
  }

  #ui-ux-patterns {
    padding-bottom: 50px;
  }

  #agile-scrum {
    .icon-section {
      flex-direction: row;
      margin-top: 40px;
      .icon-content {
        margin: 0 15px;
      }
    }
    .lower-scrum {
      background-position: bottom;
    }
  }

  #inbound-marketing {
    margin-bottom: 60px;
  }
}
</style>
