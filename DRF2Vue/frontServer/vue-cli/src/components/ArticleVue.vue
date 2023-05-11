<template>
  <div>
    <hr>
    <p>글 번호 : {{article?.id}}</p>
    <p> 글 제목 : {{article?.title}}</p>
    <p> 글 내용 : {{article?.content}}</p>
    <!-- 이렇게 하려면 article을 언급해야 함 -->
    <router-link :to="{
      name: 'DetailView',
      params:{id:article.id}}">
      [DETAIL]
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'ArticleVue',
  props:{
    article:Object,
  }


}
</script>

<style>

</style>