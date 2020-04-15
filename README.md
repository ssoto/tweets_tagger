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
### Run server
And just run it using `uvicorn`:
```shell script
uvicorn tweet_tagger.main:api --debug
```
In order to test API you can load:
* <a href="http://127.0.0.1:8000/docs" target="_blank">OpenAPI endpoint</a>

or / and
* <a href="http://127.0.0.1:8000/redoc" target="_blank">Redoc endpoint</a>

There you can read endpoints documentation, but by the moment no data has been imported... it's time to do it!
## Tweet data importation
The app use `MongoDB` so you need install it. You process documenation on it's own webpage: 
<a href="https://docs.mongodb.com/manual/installation/" target="_blank">mongodb.com</a>

One you have done, its time to donwload data and import into database.

### Download tweets to a CSV
We used <a href="https://github.com/Mottl/GetOldTweets3" target="_blank">GetOldTweets3 module</a> to download tweets. With this command you will download all tweets at 10 kms from Seville related with `Coronavirus` and `Holy Week`  in Spanish language:
```shell script
GetOldTweets3 --querysearch "coronaviru+semana+santa" --near "Sevilla" --within 10km --maxtweets 100 --lang es
```
The default output csv file name is `output_got.csv`. Suppose you download tweets on your `~/data/` folder.
### Tweett CSV importation
Now you must to use this script to import in mongodb:
```shell script
python bin/import_tweets.py --csv-path ~/data/output_got.csv
```
This simple scripts uses mongodb and CSV path settings defined on `tweet_tagger.settings` module.

# Frontend configure and installation
We need install `Node.js` to build frontend code. You can use `vnm` utility to manage node installation. 
Currently we are using `12.16`: 
```shell script
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
NODE_VERSION=12.16.2
nvm install $NODE_VERSION
nvm use $NODE_VERSION
```
Now time to install dependencies and compile frontend:
```shell script
cd web
npm install
npm run build
```
Now you can tagger your tweets on [http://127.0.0.1:8000](http://127.0.0.1:8000)

This built code has been served by our fastapi [server that must to be running](run-server)

