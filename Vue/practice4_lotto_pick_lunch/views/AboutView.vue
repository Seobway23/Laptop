<template>
  <div class="about">
    <h1>로또</h1>
    <button @click="getLucky"> Get Lucky Numbers</button>
    <p>{{numbers}}</p>
  </div>
</template>
<script>
import _ from 'lodash'

export default {
  name: 'getLucky',
  data(){
    return{
      numbers:null,
    }
  },
  methods:{
    getLucky(){
      const number = _.sampleSize(_.range(1,46),6)
      this.numbers = number
    }
  }

}
</script>