<template>
  <div>
    <div class="card">
    <img class="" :src="posterPath" alt="movie poster">  
      <div class="card-body">
        <h5 class="card-title">{{randomMovie.title}}</h5>
        <p class="card-text">{{randomMovie.overview}}</p>
        <p class="card-text"><small class="text-body-secondary">vote_count : {{randomMovie.vote_count}}</small></p>
      </div>  
    </div>
  </div>
</template>

<script>
  import _ from "lodash"
  // const Movies = this.$store.state.movies
  // const b =  _.random([0], [20])
  // console.log(b)
  export default {
    name:'RandomView',
    data(){
    return {

    }
  },
  created() {
    this.fetchPopularMovies()
  },
  methods:{
    fetchPopularMovies() {
      this.$store.dispatch('fetchPopularMovies')
    },

    getRandomMovie(){
      // console.log(this.movies)
      // console.log(1)
      const b =  _.random([0], [this.movies.length])
      return this.movies[b]
    }

  },
  computed:{
    movies(){
      return this.$store.state.movies
    },
    randomMovie(){
      // 랜덤으로 가져올게 (pk로 가져올게 라는 로직이 들어갑니다.)
      const movie = this.getRandomMovie(this.$store.state.movies)
      return movie
    },
    posterPath() {
      const baseUrl = 'https://image.tmdb.org/t/p/'
      const pathUrl = this.randomMovie.poster_path
      const posterUrl = baseUrl + 'w300' + pathUrl
      return posterUrl
    }
  },


  }
</script>

<style>

</style>