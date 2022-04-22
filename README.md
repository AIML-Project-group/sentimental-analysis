# Twitter Sentiment Analysis

A webapp to visualize sentiment on a given topic as per recent tweets.


- [Twitter Sentiment Analysis](#twitter-sentiment-analysis)
  - [Running Locally](#running-locally)

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
