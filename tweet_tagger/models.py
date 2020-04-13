import traceback

from fastapi import HTTPException

from tweet_tagger import settings


class TweetModel:

    def __init__(self, json: dict):
        self.json = json

    def as_json(self):
        return self.json

    @classmethod
    def update_tweet_category(cls, tweet_id, category):
        result = settings.TWEETS_COL.update(
            {'_id': tweet_id},
            {'$set': {'category': category}},
        )
        return result


class TweetsFactory:

    @classmethod
    def retrieve_untagged_tweet(cls, tweet_id: int):
        if not tweet_id:
            return cls.get_untagged_tweet()
        else:
            return cls.get_tweet(tweet_id)

    @classmethod
    def get_untagged_tweet(cls):
        try:
            return TweetModel(settings.TWEETS_COL.find_one(
                {'category': {'$exists': False}}
            ))
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail='{}'.format(traceback.extract_stack())
            )

    @classmethod
    def get_tweet(cls, tweet_id: int):
        result = settings.TWEETS_COL.find_one({'_id': tweet_id})
        if not result:
            # FIXME: this behaviour should be in api code not in model
            raise HTTPException(
                status_code=204,
                detail=f'Tweet with {tweet_id} doesn\'t find.')
        return TweetModel(json=result)