<template>
  <div>
   <h1>Articles</h1>
   <ArticleVue
   v-for="article in articles" :key="article.id" :article="article"
   />
  </div>
</template>

<script>
import ArticleVue from '@/components/ArticleVue.vue'

export default {
  name: 'ArticlesVue',
  components:{
    ArticleVue,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }

}
</script>

<style>
.article-list {
  text-align: start;
}
</style>

