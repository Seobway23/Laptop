<template>
<div>
  <h1>
    watch list vue
  </h1>
  <WatchListForm/>
  <WatchList/>
</div>
  
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue'

export default {
  name: 'WatchListView',
  components: {
    WatchListForm
  }
}
</script>

<style>

</style>