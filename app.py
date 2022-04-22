import streamlit as st
from src.twitter import get_tweets
from src.utils import clean_df
from src.prediction import predict

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.use('agg')

def main():
  st.title('Twitter sentimental Analysis')
  st.subheader('Enter a topic below to get sentimental view of the topic')

  topic = str(st.text_input('Input a trending topic'))

  if len(topic) > 0:
    with st.spinner('Please wait till tweets are being extracted'):
      df = get_tweets(topic)

    df = clean_df(df)
    df['sentiment'] = df['tweet'].apply(predict)

    st.write(f'Total tweets extracted for "{topic}" are {df.tweet.count()}')
    st.write(f'Total Positive Tweets are : {len(df[df["sentiment"]=="Positive"])}')
    st.write(f'Total Negative Tweets are : {len(df[df["sentiment"]=="Negative"])}')
    st.write(f'Total Neutral Tweets are : {len(df[df["sentiment"]=="Neutral"])}')  


if __name__ == '__main__':
  main()
