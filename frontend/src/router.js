import Vue from 'vue';
import Router from 'vue-router';
import store from '@/store';

import Start from '@/views/Start.vue';
import Instructions from '@/views/Instructions.vue';
import Upload from '@/views/Upload.vue';
import Style from '@/views/Style.vue';
import Share from '@/views/Share.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'start',
      component: Start,
    },
    {
      path: '/instructions',
      name: 'instructions',
      component: Instructions,
    },
    {
      path: '/upload',
      name: 'upload',
      component: Upload,
    },
    {
      path: '/style',
      name: 'style',
      component: Style,
    },
    {
      path: '/share',
      name: 'share',
      component: Share,
      beforeEnter(to, from, next) {
        const { originalImage, style } = store.state;
        if (!originalImage) {
          next('/upload');
        } else {
          store.dispatch('uploadImage');
          next();
        }
      },
    },
  ],
});
