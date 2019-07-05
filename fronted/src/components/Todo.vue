<template>
  <div class="container">
    <h1 class="text-center">Customers information</h1>
    <div class="row">
      <div class="col-lg-2">
        <label class="radio-inline"><input type="radio" name="optradio" v-on:click = "getCustomersBySegment('0')" checked>All segments</label>
        <hr>
        <label class="radio-inline"><input type="radio" name="optradio" v-on:click = "getCustomersBySegment('1')">Segment 1</label>
        <label class="radio-inline"><input type="radio" name="optradio" v-on:click = "getCustomersBySegment('2')">Segment 2</label>
        <label class="radio-inline"><input type="radio" name="optradio" v-on:click = "getCustomersBySegment('3')">Segment 3</label>
        <label class="radio-inline"><input type="radio" name="optradio" v-on:click = "getCustomersBySegment('4')">Segment 4</label>
        <label class="radio-inline"><input type="radio" name="optradio" v-on:click = "getCustomersBySegment('5')">Segment 5</label>
        <hr>
        <label><b>Sort by</b></label>
        <label class="radio-inline"><input type="radio" name="optradio1" v-on:click = "sortBy('id')" checked>Id</label>
        <label class="radio-inline"><input type="radio" name="optradio1" v-on:click = "sortBy('years_customer')">Years_customer</label>
        <label class="radio-inline"><input type="radio" name="optradio1" v-on:click = "sortBy('no_of_complaints')">No_of_complaints</label>
        <label class="radio-inline"><input type="radio" name="optradio1" v-on:click = "sortBy('contract_value')">Contract_value</label>
        <label class="radio-inline"><input type="radio" name="optradio1" v-on:click = "sortBy('gender')">Gender</label>
      </div>
      <div class="col-lg-7">
        <table class="table">
          <tr>
            <td style="color: #3e88f0;"><b>Id</b></td> 
            <td style="color: #3e88f0;"><b>Gender</b></td> 
            <td style="color: #3e88f0;"><b>Segment</b></td> 
            <td style="color: #3e88f0;"><b>Years_customer</b></td> 
            <td style="color: #3e88f0;"><b>No_of_complaints</b></td> 
            <td style="color: #3e88f0;"><b>Contract_value</b></td> 
          </tr>
          <tr v-for="(customer, index) in Customers" :key="index">
            <td>{{customer.id}}</td> 
            <td>{{customer.gender}}</td> 
            <td>{{customer.segment}}</td> 
            <td>{{customer.years_customer}}</td> 
            <td>{{customer.no_of_complaints}}</td> 
            <td>{{customer.contract_value}}</td> 
          </tr>
        </table> 
      </div>
      <div class="col-lg-3"><barchart v-if="this.chartFlag" :data="this.arrayParams"/></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import BarChart from './BarChart'
import _ from 'lodash';

export default {
  components: {
    barchart : BarChart
  },
  data() {
    return {
      Customers: [],
      id : '0',
      sortElem : '',
      averageYears : 0,
      averageComplains : 0,
      chartFlag : true,
      arrayParams : [],
    };
  },
  mounted () {
    this.getCustomersBySegment(this.id)
  }, 
  methods: {
    getCustomersBySegment(segment_id) {
      this.chartFlag = false
      this.id = segment_id
      const path = 'http://localhost:5000/';
      axios.get(path, {params: {id: segment_id}})
      .then((res) => {
          this.Customers = res.data.data;
          this.averageYears = res.data.years;
          this.averageComplains = res.data.complains;
          let idSegment = ""
          if(this.id == '0')
            idSegment = 'All segments'
          else {
            idSegment = "Segment " + this.id
          }
          this.arrayParams = [this.averageYears,this.averageComplains,idSegment]
          this.chartFlag = true
          this.sortBy(this.sortElem)
          console.log(res)
        })
        .catch((error) => {
          console.error(error);
        });

    },
    sortBy(sorting_element) {
      this.sortElem = sorting_element
      this.Customers = _.sortBy(this.Customers, [this.sortElem]);
    },
  }
};
</script>
