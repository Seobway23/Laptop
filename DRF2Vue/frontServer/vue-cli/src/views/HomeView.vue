<template>
  <div class="home">
    <img alt="Vue logo" src="https://hips.hearstapps.com/hmg-prod/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=1.00xw:0.756xh;0,0.0756xh&resize=1200:*">
    <router-link :to="{name: 'CreateView'}">[CREATE]</router-link>
    <ArticlesVue/>
  </div>
</template>

<script>
// @ is an alias to /src
import ArticlesVue from '@/components/ArticlesVue.vue'

export default {
  name: 'HomeView',
  components: {
    ArticlesVue
  },
  computed:{

  },
  created() {
    this.getArticles()
    
  },
  methods: {
    getArticles(){
      this.$store.dispatch('getArticles')
    }
  },
}
</script>
