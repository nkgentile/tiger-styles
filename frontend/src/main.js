import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import store from '@/store';
import '@/plugins';
import '@/assets/styles/index.scss';

import io from 'socket.io-client';

Vue.config.productionTip = false;

const app = new Vue({
  router,
  store,
  render: h => h(App),
});

const socket = io('http://localhost:5000/style');
socket.on('connect', () => {
  console.log('Connected!');
  app.$mount('#app');
});
