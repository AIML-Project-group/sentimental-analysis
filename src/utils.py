from re import I, sub

from pandas import DataFrame
from wordcloud import STOPWORDS, WordCloud


def clean_tweet(tweet: str) -> str:
  regex = r'(^RT)|@\w+|[^0-9A-Za-z,!\':"!?\. \t]|\w+:\/\/\S+'
  return ' '.join(sub(regex, ' ', str(tweet)).split()).lower()

def clean_df(df: DataFrame) -> DataFrame:
  df['cleaned_tweet'] = df['tweet'].apply(clean_tweet)
  return df

def build_cloud(texts: str, topic: str) -> WordCloud:
  '''Returns a wordcloud for list of text for given topic'''
  topic = sub(r'[^\da-z \t]', ' ', topic, I)
  stopwords = set(STOPWORDS)
  stopwords.update(topic.split())

  new_words = ' '.join(text for text in texts.split() if text not in stopwords)
  return WordCloud(stopwords=stopwords, max_words=100, max_font_size=70).generate(new_words)
