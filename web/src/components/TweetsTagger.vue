<template>
  <div class="tweets-tagger">
    <h1>Tweets Tagger Tool</h1>
    <Tweet>

    </Tweet>
    <div class="buttons">
      <div class="action-button" :class="category" @click="sendCategory(category)"
              v-for="category in categories">
        <p class="button-title">
          <span>{{ category }}</span>
          <span class="little"> or press
            <span v-for="keyCode in keyCodes[category]" class="little-category">"{{keyCode}}" </span>
          </span>
        </p>
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
  public keyCodes: {[id: string]: string[]} = {
    positive: ['1', 'p'], // 1 and p keys
    neutral: ['2', 'k'], // 2 and m keys
    negative: ['3', 'n'],  // 3 and n keys
  };
  public sendCategory(category: string): void {
    let self = this;
    this.$store.dispatch('postTweetCategory', {
      id: self.tweet.tweet_id,
      category: category,
      ... {
        callback() {
          self.$store.dispatch('loadTweet');
        },
      },
    });
  }
  private mounted() {
    let self = this;
    this.$store.dispatch('loadTweet');
    window.addEventListener('keydown', event => {
      for(let categoryIndex in self.categories){
        const category = self.categories[categoryIndex];
        if(self.keyCodes[category].includes(event.key)) {
          self.sendCategory(category);
        }
      }
    });
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

.action-button > p {
  display: inline;
}

.little {
  color: #808080;
  font-size: 10px;
  font-weight: bold;
  text-transform: lowercase;
}

.little-category:last-child::before{
  content: 'or '
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
