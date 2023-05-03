<template>
  <div id="app">
    <button @click="toogle">toggle</button>
    <DogComponent/>

    <h1>이곳은 App.vue 입니다.</h1>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="5월 3일은 특별한 날입니다."
    @event-name="arlertValue"/>
    <MyComponent/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from '@/components/MyComponent.vue' // 1. 불러온다
import DogComponent from '@/components/DogComponent.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent, // 2.등록한다
    DogComponent,
  },
  methods:{
    arlertValue(obj) {
      alert(obj.data)

    },
    toggle() {
      this.flag = !this.flag
    }
  },
  created() {
    console.log('App created! 앱이 만들어졌음')
  },
  mounted() {
    console.log('App mounted!')
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
