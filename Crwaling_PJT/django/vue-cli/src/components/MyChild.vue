<template>
  <div>
    <h3>This is the child component</h3>
    <p>{{staticProps}}</p>
    <p>{{dynamicProps}}</p>
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  props: {
    staticProps:String,
    dynamicProps:String,
  }
}
</script>

<style>

</style>