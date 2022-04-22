from json import load
from pathlib import Path

from pandas import DataFrame
from tweepy import API, OAuth2BearerHandler

envpath = (Path(__file__).parent.parent/'env.json').absolute()
try:
  env = load(open(envpath))
except FileNotFoundError:
  env = {}

auth = OAuth2BearerHandler(env.get('bearer_token'))
api = API(auth)

def get_api():
  global api
  return api

def get_tweets(topic):
  global api
  topic = f'{topic} -filter:retweets'
  df = DataFrame(columns=['date', 'user', 'is_verified', 'tweet', 'likes', 'retweets', 'user_location'])
  
  # Twitter returns max 100 tweets per query
  for i, tweet in enumerate(api.search_tweets(topic, lang='en', count=100, tweet_mode='extended')):
    df.loc[i, 'date'] = tweet.created_at
    df.loc[i, 'user'] = tweet.user.name
    df.loc[i, 'is_verified'] = tweet.user.verified
    df.loc[i, 'tweet'] = tweet.full_text
    df.loc[i, 'likes'] = tweet.favorite_count
    df.loc[i, 'retweets'] = tweet.retweet_count
    df.loc[i, 'user_location'] = tweet.user.location
  return df
