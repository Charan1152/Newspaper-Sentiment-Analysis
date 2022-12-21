import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

# Replace YOUR_API_KEY with your actual API key
api_key = "abe931fb3f5d448a97472793f9fb8853"

# Set the API endpoint URL and the desired parameters
api_endpoint = "https://newsapi.org/v2/top-headlines"
params = {
    "apiKey": api_key,
    "language": "en"
}

# Make the API request to retrieve the articles
response = requests.get(api_endpoint, params=params)
# Extract the list of articles from the response
articles = response.json()["articles"]

# Initialize the sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()
i=1
# Iterate over each article
for article in articles:
    # Extract the text of the article
    text = article["description"]

    # Use the sentiment analyzer to classify the sentiment of the text
    sentiment = sentiment_analyzer.polarity_scores(text)
    # Print the sentiment of the article
    print("Article {}: {}".format(i,article['description']))
    print("-> The article is {}% positive, {}% negative and {}% neutral.".format(sentiment['pos'] * 100, sentiment['neg'] * 100, sentiment['neu'] * 100))
    print("\n\n")
    i+=1

