<template>
  <div class="hello">
    <h1>이곳은 HelloWorld.vue 입니다.</h1>
    <br>
    <br>
    <br>
    <h4>SSAFY 여러분을 응원합니다.</h4>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
