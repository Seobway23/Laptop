<template>
  <div>
    <button @click="getDogImage"> 멍멍아 이리온</button>
    <img v-if="imgSrc" :src="imgSrc" alt="#"> <br>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogComponent',
  data() {
    return {
      imgSrc : null,
  }
  },
  methods:{
    getDogImage() {
      const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'

      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response)=> {
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error)=> {
          console.log(error)
        })
    }
  },
  created() {
    this.getDogImage()
    console.log('Dog created!')
  },
  mounted() {
    console.log('Dog mounted!')
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
  },
  updated() {
    console.log('새로운 멍멍이!')
    console.log('Dog updated!')
  }
} 
</script>

<style>

</style>