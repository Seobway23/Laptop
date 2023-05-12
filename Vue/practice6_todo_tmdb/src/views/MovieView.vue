<template>
  <div>
    <h1>hello</h1>
    <div class="card-group">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
      <!-- <p>{{movie.vote_count}}</p> -->
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieView',
  props: {
    movie: Object,
  },
  components: {
    MovieCard
  },
  data(){
    return {
      // movies: []
    }
  },
  computed:{
    movies(){
      return this.$store.state.movies
    }
  },
  created() {
    this.fetchPopularMovies()
  },
  methods: {
    fetchPopularMovies() {
      this.$store.dispatch('fetchPopularMovies')
    .then((res)=>{
      console.log(res)
    })
    }
  }

}
</script>
