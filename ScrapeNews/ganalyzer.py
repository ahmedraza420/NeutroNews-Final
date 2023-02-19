
# set GOOGLE_APPLICATION_CREDENTIALS="Users\behes\OneDrive\Desktop\FYP\Final Sentiment\clash-of-clans-179107-cdbdd23e5bc8.json"

from google.cloud import language_v1beta2
from google.cloud.language_v1beta2 import types
from google.oauth2 import service_account


creds = service_account.Credentials.from_service_account_file("ScrapeNews\clash-of-clans-179107-cdbdd23e5bc8.json")

client = language_v1beta2.LanguageServiceClient(credentials=creds)

article = """
An earthquake with a magnitude of 5.9 struck northwest Iran near the border with Turkey on Saturday, killing at least three people and injuring more than 300, state media reported. The official news agency IRNA reported the toll citing the head of emergency services at the university in the city of Khoy, near the quake’s epicentre. An emergency official told state TV that it was snowing in some of the affected areas, with freezing temperatures and some power cuts reported. Major geological faultlines crisscross Iran, which has suffered several devastating earthquakes in recent years Comments
"""


def get_sentiment_score(text):
    """
Analyzes the sentiment score of the input text
arguments:
        text (string): The input text for sentiment analysis.

returns:
        sentiment_score (float): Representing the sentiment of the text (between -1 and 1)
        1: postive
        0: neutral
        -1: negative
    """
    sentiment_score = 0

    document = language_v1beta2.Document(content= text, type = language_v1beta2.Document.Type.PLAIN_TEXT)
    sentiment_score = client.analyze_sentiment(
        request = {"document": document}
        ).document_sentiment.score

    #sentiment_score = client.analyze_sentiment(document=document).document_sentiment.score
    return sentiment_score

def get_sentiment(text):
    """
    Returns the sentiment of the text 

arguments:
    text (string): The input text for sentiment analysis.

returns:
    sentiment (string): representing the sentiment of the input text, 
    with 5 possible values: negative, fairly negative, neutral, fairly positive, and positive.
    """
    score = get_sentiment_score(text)
        
    if score > 0:
        if score > 0.2:
            sen = "positive"
        else:
            sen = "fairly positive"
    elif score < -0.2:
        if score < -0.3:
            sen = "negative"
        else:
            sen = "fairly negative"
    else:
        sen = "neutral"
    return {
        'sentiment' : sen,
        'score' : score
            }





