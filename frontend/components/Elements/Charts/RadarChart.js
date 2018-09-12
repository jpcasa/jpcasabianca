import { Radar } from 'vue-chartjs'

export default {
  extends: Radar,
  data() {
    return {
      options: {
        responsive: true,
        maintainAspectRatio: true,
        legend: {
          display: false
        },
        scale: {
          ticks: {
            beginAtZero: true,
            min: 0,
            max: 10,
            stepSize: 2
          }
        }
      }
    }
  },
  props: ['data'],
  mounted () {
    this.renderChart(this.data, this.options)
  }
}
