<template>
  <div class='border'>
    <h1> This is Component</h1>
    <MyChild static-props="component에서 child로"
    :dynamic-props="dynamicProps"
    />

  </div>
</template>

<script>
import MyChild from '@/components/MyChild.vue'

export default {
  name: 'MyComponent',
    components: {
    MyChild,
  },
  data: function () {
    return{
    dynamicProps : "it's in data"    
    }
  }

}
</script>

<style>
.border {
  border:solid;
}
</style>