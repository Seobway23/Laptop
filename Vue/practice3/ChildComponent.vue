<template>
  <div>
    value : {{value}}
    <button @click="changeValue">change value</button>
  </div>
</template>

<script>
export default {
  name: 'ChildComponent',
  data()  {
    return {
      value:0,
    }
  },
  methods: {
    changeValue(){
      this.value = this.value + 1
    }
  }
  
}
</script>


<style>

</style>