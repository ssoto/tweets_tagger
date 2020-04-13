<template>
  <div>
    <p class="tweet">
    {{ tweet.text }}
    </p>
    <p class="links">
      <a :href="tweet.permalink">{{ tweet.date }}</a>  |
      <a :href="'https://twitter.com/@' + tweet.username">@{{ tweet.username }}</a>
    </p>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';
  import { mapGetters } from 'vuex';
  @Component({
      computed: mapGetters(['tweet']),
  })
  export default class Tweet extends Vue {
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  text-align: right;
  margin: auto 100px;
  background-color: #E0F1F3;
  border-radius: 12px;
  padding: 12px;
}
p.tweet {
  text-align: center;
  font-style: italic;
}

p.links {
  text-align: right;
}

a {
  color: #42b983;
}
.tweets-tagger > button {
  text-transform: capitalize;
}
</style>
