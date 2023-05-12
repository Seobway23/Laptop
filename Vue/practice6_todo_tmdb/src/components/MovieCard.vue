<template>
  <div>
    <div class="card">
    <img class="" :src="posterPath" alt="movie poster">  
      <div class="card-body">
        <h5 class="card-title">{{movie.title}}</h5>
        <p class="card-text">{{movie.overview}}</p>
        <p class="card-text"><small class="text-body-secondary">vote_count : {{movie.vote_count}}</small></p>
      </div>  
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },

  computed: {
    posterPath() {
      const baseUrl = 'https://image.tmdb.org/t/p/'
      const pathUrl = this.movie.poster_path
      const posterUrl = baseUrl + 'w200' + pathUrl
      return posterUrl
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

</style>
