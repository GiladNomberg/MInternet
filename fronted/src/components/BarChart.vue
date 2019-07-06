<script>
import { Bar } from 'vue-chartjs';

export default {
   extends: Bar,
    props : {
       data : Array
   },
   data() {
      return {
         datacollection: {
            labels: ['customer years avg','complains avg'],
            datasets: [{
               backgroundColor: '#249EBF',
               label : this.data[2],
               data: [this.data[0],this.data[1]]
            }]
         },
         options: {
            scales: {
               yAxes: [{
                  ticks: {
                     beginAtZero: true
                  },
               }],
            },
            maintainAspectRatio: false
         }
      }
   },
   mounted() {
      this.renderChart(this.datacollection, this.options)
   }
}
</script>