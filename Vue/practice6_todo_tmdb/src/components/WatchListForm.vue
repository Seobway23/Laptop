<template>
  <div>
    <div>
      <h2>보고싶은 영화</h2>
      <input type="text" v-model.trim="todoTitle" @keyup.enter="createMovie">
      <button @click='createMovie'> add</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      movieTitle: null,
    }
  },
  methods: {
    createMovie(){
      if (this.movieTitle) {
        this.$store.dispatch('createMovie', this.movieTitle)
      } else {
        alert('제목을 입력하세요!')
      }
      this.movieTitle = null
    }
}
}
</script>

<style>

</style>
