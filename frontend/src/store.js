import Vue from 'vue';
import Vuex from 'vuex';

import * as uuid from 'uuid/v4';

import io from 'socket.io-client';
const socket = io('http://localhost:5000/style');

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    clientId: uuid(),
    originalImage: null,
    styledImage: null,
    style: 'tony',
  },
  mutations: {
    setOriginalImage: (state, { file }) => {
      state.originalImage = file;
    },
    setStyledImage: (state, { file }) => {
      state.styledImage = file;
    },
    setStyle: (state, { id }) => {
      state.style = id;
    },
  },
  actions: {
    uploadImage({ state }) {
      const { clientId, style, originalImage } = state;
      socket.binary(true).emit('upload', {
        id: clientId,
        style: style,
        content: originalImage,
      });
    },
  },
});

socket.on('success', data => {
  console.log(data);
  const file = new Blob([new Uint8Array(data)]);
  store.commit('setStyledImage', { file });
});

export default store;
