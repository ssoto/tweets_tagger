<template>
  <div id="app">
    <TweetsTagger />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import TweetsTagger from './components/TweetsTagger.vue';

@Component({
  components: {
    TweetsTagger,
  },
})
export default class App extends Vue {}
</script>

<style>
body {
  background-color: #F3EAE0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #505050;
  background-color: white;
  border-radius: 60px;
  margin-top: 120px;
  margin-left: 60px;
  margin-right: 60px;
  padding: 30px;
}
</style>
