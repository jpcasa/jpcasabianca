<template>
  <section>

    <section id="digital-world">
      <div class="container text-center">
        <SimpleTitle
          id="simple-title-digital"
          class="text-center"
          title="Experience &amp; Work"
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
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
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
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
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
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
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
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
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
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
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
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
          subtitle="A short story"
          copy="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad."
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
          'copy': '1Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.'
        },
        {
          'id': 1,
          'title': '2.<br>Define',
          'img': 'img/define.svg',
          'copy': '2Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.'
        },
        {
          'id': 2,
          'title': '3.<br>Ideate',
          'img': 'img/ideate.svg',
          'copy': '3Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.'
        },
        {
          'id': 3,
          'title': '4.<br>Prototype',
          'img': 'img/prototype.svg',
          'copy': '4Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.'
        },
        {
          'id': 4,
          'title': '5.<br>Test',
          'img': 'img/test.svg',
          'copy': '5Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat.'
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
          'subtitle': 'Lorem ipsum dolor sit amet',
          'copy': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.'
        },
        {
          'icon': 'img/scrum-master.svg',
          'title': 'Scrum Master',
          'subtitle': 'Lorem ipsum dolor sit amet',
          'copy': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.'
        },
        {
          'icon': 'img/dev-team.svg',
          'title': 'Dev Team',
          'subtitle': 'Lorem ipsum dolor sit amet',
          'copy': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.'
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
