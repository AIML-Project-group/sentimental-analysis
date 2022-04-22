import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from src.prediction import predict
from src.twitter import get_tweets
from src.utils import build_cloud, clean_df

matplotlib.use('agg')
plt.style.use('dark_background')

def main():
  st.title('Twitter sentimental Analysis')
  st.subheader('Enter a topic below to get sentimental view of the topic')

  topic = st.text_input('Input a trending topic', key='topic')

  if len(topic) > 0:
    with st.spinner('Please wait till tweets are being extracted'):
      df = get_tweets(topic)

    df = clean_df(df)
    df['sentiment'] = df['tweet'].apply(predict)

    positive_tweets = df[df['sentiment'] == 'Positive'].shape[0]
    negative_tweets = df[df['sentiment'] == 'Negative'].shape[0]
    neutral_tweets = df[df['sentiment'] == 'Neutral'].shape[0]

    labels = ['Positive', 'Neutral', 'Negative']

    # Summary
    st.subheader('Summary')
    col1, col2 = st.columns([2, 1])
    col1.write(f'Total tweets extracted for "{topic}" are {df.tweet.count()}')
    col1.write(f'Total Positive Tweets are : {positive_tweets}')
    col1.write(f'Total Negative Tweets are : {negative_tweets}')
    col1.write(f'Total Neutral Tweets are : {neutral_tweets}')  

    # Pie chart at the right
    fig, ax = plt.subplots()
    ax.pie([positive_tweets, neutral_tweets, negative_tweets],
      shadow=True, explode=(0.1, 0, 0.1), autopct='%1.2f%%',
      labels=labels)
    col2.pyplot(fig)

    # Count plot based on verified and unverified users
    if st.button('Get sentiments based on authencity of users'):
      st.success('Generating a count plot...')
      st.subheader('Count plot for verified and unverified users')
      fig = plt.figure()
      sns.countplot(x=df['sentiment'], hue=df.is_verified)
      st.pyplot(fig)

    # Wordcloud for each type of sentiment
    for l in labels:
      if st.button(f'Visualize {l} tweets'):
        st.subheader(f'Wordcloud for {l} tweets')
        words = ' '.join(df[df['sentiment'] == l].cleaned_tweet.tolist())
        cloud = build_cloud(words, topic)
        fig= plt.figure()
        plt.imshow(cloud)
        st.pyplot(fig)


if __name__ == '__main__':
  main()
