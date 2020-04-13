#!/usr/bin/python
# -*- coding: UTF-8 -*-
# System imports
# Third party imports
from fastapi import FastAPI, HTTPException
# Local imports
from tweet_tagger.models import TweetsFactory, TweetModel

TWITTER_CATEGORIES = ['neutral', 'negative', 'positive', ]

api = FastAPI()


@api.get("/")
def read_root():
    return {"Hello": "World"}


@api.get('/tweet')
def retrieve_tweet(tweet_id: int = None):
    """Return tweet with the given identifier"""
    if not tweet_id:
        return TweetsFactory.get_untagged_tweet().as_json()

    else:
        return TweetsFactory.get_tweet(tweet_id=tweet_id).as_json()

@api.post('/tweet')
def update_post_category(tweet_id: int, category: str):
    if category not in TWITTER_CATEGORIES:
        raise HTTPException(
            status_code=400,
            detail='invalid category, valida values are: {}'.format(TWITTER_CATEGORIES)
        )
    TweetModel.update_tweet_category(tweet_id, category)

