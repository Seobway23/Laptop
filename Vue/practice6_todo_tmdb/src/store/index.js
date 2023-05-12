import Vue from 'vue'
import Vuex from 'vuex'


import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    movieitems: [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies){
      state.movies = movies
    },

    CREATE_MOVIE(state, movieItem) {
      state.movieitems.push(movieItem)
      // console.log(state.todos)
    }

  },
  actions: {
    fetchPopularMovies(context) {
      if (!context.state.movies.length){
      const apiKey = '256b61b60a713d12f9806d31ce87c1dc'
      const movieurl = `https://api.themoviedb.org/3/movie/popular?api_key=${apiKey}`

      axios({
        method: 'get',
        url: movieurl,
        
      })
      .then((res)=> {
        // console.log(res.data.results)
        // this.movies = res.data.results
      
        const movies = res.data.results
        context.commit('GET_MOVIES', movies)
      })
      .catch((err)=>{
        console.log(err)
      })
    } else{
      return
    }
    },

    createMovie(context, movieTitle) {
      const movieItem = {
        title: movieTitle,
      }
      // console.log(todoItem)
      context.commit('CREATE_MOVIE',movieItem)
    }
    },
  modules: {
  }
})
