import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import bootstrap from 'bootstrap/dist/css/bootstrap.css';


Vue.config.productionTip = false

new Vue({
  router,
  store,
  bootstrap,
  render: h => h(App)
}).$mount('#app')
