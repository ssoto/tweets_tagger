<template>
  <div class="tweets-tagger">
    <h1>Tweets Tagger Tool</h1>
    <Tweet>

    </Tweet>
    <div class="buttons">
      <div class="action-button" :class="category" @click="sendCategory(category)"
              v-for="category in categories">
        {{ category }}
      </div>
    </div>

  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Tweet from './Tweet.vue';
import { mapGetters } from 'vuex';

@Component({
  components: {
    Tweet,
  },
  computed: mapGetters(['tweet']),
})
export default class TweetsTagger extends Vue {
  private tweet: any;
  private categories: string[] = [
    'positive', 'neutral', 'negative',
  ];
  public sendCategory(category: string): void {
    let self = this;
    this.$store.dispatch('postTweetCategory', {
      id: self.tweet._id,
      category: category,
      ... {
        callback() {
          self.$store.dispatch('loadTweet');
        },
      },
    });
  }
  private mounted() {
    this.$store.dispatch('loadTweet');
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tweets-tagger{
  display: inline-block;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.buttons {
  display: inline-block;
  margin-top: 20px;
}
.action-button {
  margin-top: 12px;
  display: inline;
  margin-left: 20px;
  font-size: 14px;
  font-weight: bold;
  padding: 12px;
  border-radius: 6px;
  text-transform: capitalize;
  cursor: default;
}

.positive {
  background-color: lightgreen;
}
.negative {
  background-color: lightcoral;
}
.neutral {
  background-color: lightyellow;
}
</style>
