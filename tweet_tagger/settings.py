from pymongo import MongoClient

MONGO_CONN = MongoClient('127.0.0.1')
TWEET_TAGGER_DB = MONGO_CONN['tweet_tagger']
TWEETS_COL = TWEET_TAGGER_DB['tweets']
