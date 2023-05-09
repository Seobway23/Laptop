<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <h1>점심메뉴</h1>
    <button @click="pickLunch"> Pick Lunch</button>
    <p>{{lunch}}</p>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  data(){
    return{
      lunch:null,
    }
  },
  components: {
    HelloWorld
  },
  methods:{
    pickLunch(){
      const lunchOptions = ['Pizza', 'Burger', 'Salad', 'Sushi']
      const randomIndex = Math.floor(Math.random() * lunchOptions.length)
      this.lunch = lunchOptions[randomIndex]
    }
  }
}
</script>
