<template>
  <div class="container">
    <h1 class="text-center">Customers information</h1>
    <div class="row">
      <div class="col-lg-2">
        <div v-for="(segment, index) in segments" :key="index">
          <label><input type="radio" name="segmentRadio" v-on:click = "getCustomersBySegment(segment)" checked>{{segment}}</label>
        </div>  
        <label><b>Sort by</b></label>
        <div v-for="(sort) in sortBy" :key="sort">
          <label><input type="radio" name="sortRadio" v-on:click = "sorting(sort)" checked>{{sort}}</label>
        </div>
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
          <tr v-for="(customer, index) in customers" :key="index">
            <td>{{customer.id}}</td> 
            <td>{{customer.gender}}</td> 
            <td>{{customer.segment}}</td> 
            <td>{{customer.years_customer}}</td> 
            <td>{{customer.no_of_complaints}}</td> 
            <td>{{customer.contract_value}}</td> 
          </tr>
        </table> 
      </div>
      <div class="col-lg-3">
        <barchart v-if="this.chartFlag" :data="this.arrayParams"/>
      </div>
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
      customers: [],
      segments : ['Segment 1','Segment 2','Segment 3','Segment 4','Segment 5','All segments'],
      sortBy : ['no_of_complaints','years_customer','contract_value','gender','id'],
      id : 'All segments',
      sortElem : 'id',
      averageYears : 0,
      averageComplains : 0,
      chartFlag : true,
      arrayParams : [],
      startFlag : true,
    };
  },
  mounted () {
    this.getCustomersBySegment(this.id)
  }, 
  methods: {
    getCustomersBySegment(segment_id) {
      if(this.id != segment_id || this.startFlag){
      this.startFlag = false  
      this.chartFlag = false
      this.id = segment_id
      const path = 'http://localhost:5000/';
      axios.get(path, {params: {id: segment_id}})
      .then((res) => {
          this.customers = res.data.data;
          this.averageYears = res.data.years;
          this.averageComplains = res.data.complains;
          let idSegment = ""
          if(this.id == '0')
            idSegment = 'All segments'
          else {
            idSegment = this.id
          }
          this.arrayParams = [this.averageYears,this.averageComplains,idSegment]
          this.chartFlag = true
          this.sorting(this.sortElem)
          console.log(res)
        })
        .catch((error) => {
          console.error(error);
        });
      }

    },
    sorting(sorting_element) {
      if(this.sortElem != sorting_element){
      this.sortElem = sorting_element
      this.customers = _.sortBy(this.customers, [this.sortElem]);
      }
    },
  }
};
</script>