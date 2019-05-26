import Vue from 'vue';

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
Vue.component('fa-icon', FontAwesomeIcon);

import { library } from '@fortawesome/fontawesome-svg-core';
import { faPortrait, faSpinner } from '@fortawesome/free-solid-svg-icons';
library.add(faPortrait, faSpinner);
