from re import sub
from pandas import DataFrame

def clean_tweet(tweet: str) -> str:
  regex = r'(^RT)|@\w+|[^0-9A-Za-z,!\':"!?\. \t]|\w+:\/\/\S+'
  return ' '.join(sub(regex, ' ', str(tweet)).split()).lower()

def clean_df(df: DataFrame) -> DataFrame:
  df['cleaned_tweet'] = df['tweet'].apply(clean_tweet)
  return df
