<template>
  <div>
    <MainHeader></MainHeader>
    <MainContent></MainContent>
    <MainFooter></MainFooter>
  </div>

</template>

<script>
import MainHeader from './components/MainHeader';
import MainContent from './components/MainContent';
import MainFooter from './components/MainFooter'



export default {
  name: 'App',

  components: {
    'MainHeader':MainHeader,
    'MainContent':MainContent,
    'MainFooter':MainFooter,

  },

  data: () => ({
    //
  }),
};
</script>
