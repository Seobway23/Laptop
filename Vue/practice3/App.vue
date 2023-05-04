<template>
  <div id="app">
    <button @click="toggle">toggle</button>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <hr>
    <ChildComponent
    v-if="flag"/>
    <DogComponent/>
    
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>

import ChildComponent from '@/components/ChildComponent.vue'
import DogComponent from './components/DogComponent.vue'

export default {
  name: 'App',
  data(){
    return{
      flag: true
    }
  },
  methods:{
    toggle() {
      this.flag = !this.flag
    }
  },
  components: {
    ChildComponent,
    DogComponent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
