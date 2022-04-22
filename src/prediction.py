from textblob import TextBlob
# from pickle import load

# __model = load(open('../model/sentiment.pkl'))

def predict(text):
  analysis = TextBlob(text)
  if analysis.sentiment.polarity > 0:
    return 'Positive'
  if analysis.sentiment.polarity == 0:
    return 'Neutral'
  return 'Negative'
