import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import UUID from 'vue-uuid'
import 'gestalt/dist/gestalt.css';

Vue.config.productionTip = false
import axios from 'axios'

Vue.prototype.axios = axios
Vue.use(UUID)
Vue.config.productionTip = false

new Vue({
  axios,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
