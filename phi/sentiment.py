from nltk.sentiment.vader import *
sid = SentimentIntensityAnalyzer()
def emotionscore(text):
    return sid.polarity_scores(text)["compound"]
