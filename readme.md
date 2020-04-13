# TLDR
We need a corpus of tweets tagged. So we build this project to obtain it fast.

## Backend installation and run
First step is clone this repository.

This project requires [mongodb installed](https://docs.mongodb.com/manual/installation/) and running on port 27017.

You will need to create a virtualenv with python3.7:
```shell script
virtualenv --python=`which python3.7` venv
source venv/bin/activate
```

Then install requirements:

```shell script
pip install -r requirements.txt
```
This projects install itself with it's own `setup.py`, you just need execute:
```shell script
pip install -e .
```

And just run it using `uvicorn`:
```shell script
uvicorn tweet_tagger.main:api --debug
```

## Tweets importation
To import builds you need first download it in CSV format, and then import into your mongodb.

### Download tweets on CSV
We used [GetOldTweets3 module](https://github.com/Mottl/GetOldTweets3) to download tweets. With this command you will 
download all tweets at 10 kms from Seville related with `Coronavirus` and `Holy Week`  in Spanish language:
```shell script
GetOldTweets3 --querysearch "coronaviru+semana+santa" --near "Sevilla" --within 10km --maxtweets 100 --lang es
```
The default output csv file name is `output_got.csv`. Suppose you download tweets on your `~/data/` folder, now you 
can use this command to import in mongodb:
```shell script
python bin/import_tweets.py --csv-path ~/data/output_got.csv

```
This simple scripts uses mongodb and CSV path settings defined on `tweet_tagger.settings` module.
