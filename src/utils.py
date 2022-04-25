from re import I, sub
from string import punctuation

from nltk import word_tokenize
from nltk.corpus import stopwords
from pandas import DataFrame
from wordcloud import STOPWORDS, WordCloud


def clean_tweet(text):
  tokens = word_tokenize(sub(r'[^a-zA-Z]', ' ', text))
  tokens = [word.lower() for word in tokens]
  text = ' '.join(tokens)
  return sub(r'https?://.+?(\s|$)', '', text)

def process_text(text):
  without_punc = ''.join(char for char in text if char not in punctuation)
  return ' '.join(word for word in without_punc.split() if word.lower() not in stopwords.words('english'))

def clean_df(df: DataFrame) -> DataFrame:
  df['cleaned_tweet'] = df['tweet'].apply(clean_tweet)
  df['cleaned_tweet'] = df['cleaned_tweet'].apply(process_text)
  return df

def build_cloud(texts: str, topic: str) -> WordCloud:
  '''Returns a wordcloud for list of text for given topic'''
  topic = sub(r'[^\da-z \t]', ' ', topic, I)
  stopwords = set(STOPWORDS)
  stopwords.update(topic.split())

  new_words = ' '.join(text for text in texts.split() if text not in stopwords)
  return WordCloud(stopwords=stopwords, max_words=100, max_font_size=70).generate(new_words)
