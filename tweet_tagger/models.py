import traceback
import json

from fastapi import HTTPException

from tweet_tagger import settings


class TweetModel:

    def __init__(self, json: dict):
        tweet_id = json.pop('_id')
        json.update({'tweet_id': tweet_id})
        self.json = json

    async def as_json(self):
        permalink = self.json['permalink']
        tweet_id = self.json['tweet_id']
        print(f'permalink is {permalink}, and tweet_id is {tweet_id}')
        return self.json

    @classmethod
    async def push_tweet_categorization(cls, tweet_id: str,
                                        category: str,
                                        user_id: str) -> dict:
        """

        :param tweet_id: tweet to update identifier
        :param category: category to assign to tweet
        :param user_id: user identifier
        :return:
        """
        result = settings.TWEETS_COL.update(
            {'_id': tweet_id},
            # {'$set': {'category': category}},
            {'$push': {'categories': {'user_id': user_id,
                                      'category': category}}}
        )
        return result


class TweetsFactory:

    @classmethod
    async def retrieve_untagged_tweet(cls, tweet_id: str):
        if not tweet_id:
            return await cls.get_untagged_tweet()
        else:
            return await cls.get_tweet(tweet_id)

    @classmethod
    async def get_untagged_tweet(cls):
        try:
            # FIXME: change pymongo with robot (async python driver)
            return await TweetModel(settings.TWEETS_COL.find_one(
                {'categories': {'$exists': False}}
            )).as_json()
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail='{}'.format(traceback.extract_stack())
            )

    @classmethod
    async def get_tweet(cls, tweet_id: str):
        result = settings.TWEETS_COL.find_one({'_id': tweet_id})
        if not result:
            # FIXME: this behaviour should be in api code not in model
            raise HTTPException(
                status_code=204,
                detail=f'Tweet with {tweet_id} hasn\'t been found.')
        return await TweetModel(json=result).as_json()
