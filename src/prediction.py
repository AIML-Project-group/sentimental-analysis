# from textblob import TextBlob
from pickle import load

__model = load(open('./model.pkl', 'rb'))
__vectorizer = load(open('./vectorizer.pkl', 'rb'))
sentiment_mappings = { 'positive': 1, 'neutral': 0, 'negative': -1 }

def predict(text):
  x = __vectorizer.transform([text])
  analysis,*_ = __model.predict(x)
  if analysis > 0:
    return 'Negative'
  if analysis == 0:
    return 'Neutral'
  return 'Positive'
