<template>
  <img :src="catUrl" alt="">  

<!-- src의 "catUrl"에서 바인드를 하지 않으면, string으로 인식하기 때문에 바인딩을 위해 src앞에 : 을 붙인다. -->

</template>


<script>
export default {
  name:"catImg",
  props:{
    catUrl: String
  }
  
}
</script>

<style>
  img{
    width: 100px;
    height: 100px;
  }
</style>