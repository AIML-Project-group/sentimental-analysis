from pickle import load
from textblob import TextBlob

# __model = load(open('../model/sentiment.pkl'))

def predict(text):
  analysis = TextBlob(text)
  if analysis.sentiment.polarity > 0:
    return 'Positive'
  if analysis.sentiment.polarity == 0:
    return 'Neutral'
  return 'Negative'
