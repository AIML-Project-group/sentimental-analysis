# Twitter Sentiment Analysis

A webapp to visualize sentiment on a given topic as per recent tweets.


- [Twitter Sentiment Analysis](#twitter-sentiment-analysis)
  - [Pre-requisites](#pre-requisites)
  - [Running Locally](#running-locally)

## Pre-requisites
- Install [Python3](https://python.org)
- Get your twitter bearer token from https://developer.twitter.com/
- Rename `env.example.json` to `env.json` and change `paste-your-token-here` with the *Actual bearer token*

## Running Locally
  - Create a new virtual environment
    ```sh
      python3 -m venv env
    ```
  - Activate new environment
    ```sh
      # Windows
      > env\Scripts\activate
      
      # Linux/Unix
      $ source env/scripts/activate
    ```
  - Install python3 requirements
    ```sh
    pip install -r requirements.txt
    ```
  
  - Start streamlit server
    ```sh
    streamlit run app.py
    ```
  - Open http://localhost:8501 to access the webapp
