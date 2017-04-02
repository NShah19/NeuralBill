from datetime import datetime
from trainingTweets import parse_csv, splitTrainingTweets
from analyzer import get_words_in_tweets, get_word_features, analyze, set_training_set
# from sentimentAnalyzer import get_classifier, analyze
import re
import tweepy
import math
import nltk
import numpy as np

consumer_key = '8n2xIVxdWhW661SSRkYMX5PWJ'
consumer_secret = 'Av9WibDlGyR5yGPvxzX7voxcXs2McHkDCFvZcqjP6nYvsYDcEa'
access_token = '848081359780302849-8UHyQfHoFhGMOVFIERZe07sEUORw3Vq'
access_token_secret = '92I4B67TMptFwuraWJKaPKvs9t4EEHzQr53w2EhFohX8a'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
subDirFiles = ["01.csv", "02.csv", "03.csv", "04.csv", "05.csv", "06.csv", "07.csv", "08.csv", "09.csv", "10.csv",
                "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv"]



#comment out everything up to classifier training below and indent everyting
"""

# Get Training Tweets
print("\033[1;33;40m Obtaining training data... \033[0m")
training_tweets = parse_csv("TrainingDataset.csv")
training_tweets = training_tweets[:2000]
print("\033[1;32;40m Training data obtained! \033[0m")

# Split the training tweets words
print("\033[1;33;40m Splitting training tweets... \033[0m")
training_tweets = splitTrainingTweets(training_tweets)
print("\033[1;32;40m Training tweets have been split! \033[0m")

# Get word features
print("\033[1;33;40m Obtaining word features... \033[0m")
word_features = get_word_features(get_words_in_tweets(training_tweets))
print("\033[1;32;40m Word Features obtained! \033[0m")

# Create the training set
print("\033[1;33;40m Creating training set... \033[0m")
training_set = set_training_set(word_features, training_tweets)
print("\033[1;32;40m Training set created! \033[0m")

# Create classifier and train!
print("\033[1;33;40m Creating classifier... \033[0m")
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("\033[1;32;40m Classifier created! \033[0m")

# classifier = get_classifier(training_tweets)
"""
tensorInputs2014 = []
tensorInputs2016 = []

tensorInputs = []

class Tweet(object):

    def __init__(self, tweetText, dateRep):
        self.text = tweetText.lower()
        self.sentiment = 0;
        self.date = dateRep

    def contains(self, kw_list):
        for kw in kw_list:
            if kw in self.text:
                return True
        return False

    def getDate(self):
        return self.date

    def getText(self):
        return self.text

    def setSentiment(self, n):
        self.sentiment = n

def isRelevant(tweet):
    if INTRODUCTION_DATE < tweet.getDate() and tweet.getDate() < VOTE_DATE and tweet.contains(listOfKW):
        return True
    return False

def weightedScore(sentiment_scores):
    score = 0;
    for sentiment, date in sentiment_scores:
        maxDaysAway = (VOTE_DATE - INTRODUCTION_DATE). days + 1
        numDaysAway = (VOTE_DATE - date).days
        value = math.expm1(3*(numDaysAway/maxDaysAway)) / math.expm1(3)
        score += sentiment * (1 - value)
    return score / len(sentiment_scores)

for filename in subDirFiles:
    parsedCSV = []
    print("opening " + filename)
    file = open("bills/" + filename)
    for line in file:
        parsedCSV.append(line[0:-1])
    billName = parsedCSV.pop(0)

    introDateList = re.split("/", parsedCSV.pop(0))
    INTRODUCTION_DATE = datetime(int(introDateList[2]), int(introDateList[0]), int(introDateList[1]))

    voteDateList = re.split("/", parsedCSV.pop(0))
    if(voteDateList[0] == 'NONE'):
        VOTE_DATE = datetime.today()
    else:
        VOTE_DATE = datetime(int(voteDateList[2]), int(voteDateList[0]), int(voteDateList[1]), 23, 59, 59)

    listOfKW = list(parsedCSV)

    if(INTRODUCTION_DATE < datetime(2017, 1, 3)):
        print("opening 2014")
        HANDLE_CSV = "handles2014.csv"
    else:
        print("opening 2016")
        HANDLE_CSV = "handles2016.csv"
    handleFile = open(HANDLE_CSV)
    listOfHandles = []
    for line in handleFile:
        listOfHandles.append(line[0:len(line) - 1])

    for handle in listOfHandles:
        tweet_contents = []
        tweet_dates = []
        last_tweet_id = 0
        oldListOfTweets = []
        sentiment_scores = []
        # Get all user tweets that arent rts or replies
        try:
            user_tweets = api.user_timeline(screen_name=handle, count=200, include_rts=False, trim_user=True, exlude_replies=True)
            # loop 3200 times
            for i in range(0,15):
                for tweet in user_tweets:
                    # append the content of the tweet to 'tweet_contents' variable
                    tweet_contents.append(tweet.text)
                    # append the date of the tweet to 'tweet_dates' varable
                    tweet_dates.append(tweet.created_at)
                    # keep track of what tweet we are on by id
                    last_tweet_id = tweet.id
                    # perform sentiment analysis on the tweet
                    #score = analyze(tweet.text, classifer)
                    #sentiment_scores.append((score, tweet.created_at))
                # set the next tweets to parse through by making the
                user_tweets = api.user_timeline(screen_name=handle, max_id=last_tweet_id-1, count=200, include_rts=False, trim_user=True, exlude_replies=True)
            # create a Tweet object using the tweet contents and datetime object and append it to tweets
            print("reached this for loop")
            for i in range(0,len(tweet_contents)):
                oldListOfTweets.append(Tweet(tweet_contents[i], tweet_dates[i]))
            listOfTweets = list(filter(isRelevant, oldListOfTweets));
            print("refined list of tweets for this handle")
            #sentiment analysis


        except tweepy.error.TweepError:
            print("EEEERRRROOOORRRRR")
            pass

    # Add weighted sentiment score for each stream to the list of tensor inputs
    #tensorInputs.append(weightedScore(sentiment_scores))
"""    numerator = 0
    denominator = 0
    for sentiment, date in sentiment_scores:
        maxDaysAway = (VOTE_DATE - INTRODUCTION_DATE).days + 1
        numDaysAway = (VOTE_DATE - date).days
        power = maxDaysAway - numDaysAway
        numerator += (sentiment * math.pow(1.2, power))
        denominator += math.pow(1.2, power)
    return numerator / denominator
"""
#    getJSON from Twitter
#    parse JSON into list of up to 3200 Tweet objects
#    filter by keyword and date
#    get sentiment analysis score for this handle based on remaining tweets
#    add this scaled score to the list of inputs to tensorFlow
#
#run tensorFlow to get prediction probability
