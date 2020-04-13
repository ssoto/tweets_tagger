import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    tweet: Object,
  },
  getters: {
    tweet: (state: any) => state.tweet,
  },
  mutations: {
    setTweet: (state, tweet) => {
      state.tweet = tweet;
    },
  },
  actions: {
    postTweetCategory: ({commit}, payload: {id: string, category: string, callback: () => void | null}) => {
      axios.post(
        `/tweet?tweet_id=${payload.id}&category=${payload.category}`,
        {tweet_id: payload.id, category: payload.category})
      .then( () => {
        if (payload.callback !== null) {
          return payload.callback();
        }
      });
    },
    loadTweet: ({commit}) => {
      axios.get('/tweet')
        .then(({data}) => {
          commit('setTweet', data);
        });
    },
  },
});
