import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)
const axios = require('axios')

export default new Vuex.Store({
  state: {
    cats:[],
  },
  getters: {
  },
  mutations: {
    CHANGE_CATS(state, catsList){
      state.cats = catsList
      console.log(state.cats)
    }
  },
  actions: {
    fetchCats(context){
      
      const url ="https://api.thecatapi.com/v1/images/search?limit=10"
      axios.get(url)
      .then(res=>{
        const catsList = res.data.map(el => el.url)
        context.commit('CHANGE_CATS', catsList)
      })
    }
  },
  modules: {
  }
})
