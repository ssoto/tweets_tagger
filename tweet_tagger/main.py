#!/usr/bin/python
# -*- coding: UTF-8 -*-
# System imports
# Third party imports
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
# Local imports
from tweet_tagger.models import TweetsFactory, TweetModel

TWITTER_CATEGORIES = ['neutral', 'negative', 'positive', ]

api = FastAPI()


@api.get('/')
def index():
    response = RedirectResponse(url='/index.html')
    return response


@api.get('/tweet')
async def retrieve_tweet(tweet_id: str = None):
    """Return tweet with the given identifier"""
    if not tweet_id:
        return await TweetsFactory.get_untagged_tweet()
    else:
        return await TweetsFactory.get_tweet(tweet_id=tweet_id)


@api.post('/tweet')
async def update_post_category(tweet_id: str, category: str):
    if category not in TWITTER_CATEGORIES:
        raise HTTPException(
            status_code=400,
            detail='invalid category, valida values are: {}'.format(TWITTER_CATEGORIES)
        )
    return await TweetModel.update_tweet_category(tweet_id, category)


api.mount("/", StaticFiles(directory="./web/dist"), name="web")
