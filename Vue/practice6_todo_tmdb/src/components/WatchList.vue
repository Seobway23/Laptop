<template>
<div>
  <WatchListItem v-for="(todo, index) in todos" :key="index" :todoitem="todo" />
</div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'
export default {
  name: 'WatchList',
  components:{
    WatchListItem
  },
  computed: {

  }
}
</script>

<style>

</style>