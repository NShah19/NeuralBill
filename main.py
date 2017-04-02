from datetime import datetime
from analyzer import analyze
import pickle
import re
import tweepy
import math
import nltk
import numpy as np

#My keys
consumer_key = 'wZD8yz1kZgsQgzsK3bNgQP2q2'
consumer_secret = 'wq0ZFMkLCei5TB2ymNoOPB6LI0188aA01Wsfs5pkQUyWA9JRr6'
access_token = '848539172298080256-AM3ev705NigIUISQLXfn4moToFQPks1'
access_token_secret = 'WiU6dcqVMs5q0g35phNrhEetKIkLhbGcXHb1XoorKLUvf'

"""
#Sachit's key:
consumer_key = 'W6CRu6R9abFdp5KagUOUuSxTT'
consumer_secret = 'bGVSXZEERi5VcfL6Polfx64ewJ2MB0VoFBXIVmsNiK861M7qLk'
access_token = '1615305834-XwgnwCCpMTd71wDOaH4PTf3jFY8V52s4IL0xeS1'
access_token_secret = 'o57Q51x743ht0W7pjeH1VK0mBP6NvnrAxXsyEYyYUCBEu'


#Nilay's Keys:
consumer_key = 'IwxM09JjCfpxwg1uupphhaCmr'
consumer_secret = 'l2z6UimZ4I9p4l2OcEM4vfkfiDBlKIkwl1404SHGUJ6PhFCTb8'
access_token = '848081359780302849-8UHyQfHoFhGMOVFIERZe07sEUORw3Vq'
access_token_secret = '92I4B67TMptFwuraWJKaPKvs9t4EEHzQr53w2EhFohX8a'
"""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#subDirFiles = ["01.csv", "02.csv", "03.csv", "04.csv", "05.csv", "06.csv", "07.csv", "08.csv", "09.csv", "10.csv",
 #               "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv"]
subDirFiles = ["06.csv"]


#comment out everything up to classifier training below and indent everyting

f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

# classifier = get_classifier(training_tweets)

tensorInputs2014 = []
tensorInputs2016 = []

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
    numerator = 0.0
    denominator = 0.0
    for sentiment, date in sentiment_scores:
        maxDaysAway = (VOTE_DATE - INTRODUCTION_DATE).days + 1
        numDaysAway = (VOTE_DATE - date).days
        power = maxDaysAway - numDaysAway
        numerator += (sentiment * math.pow(1.2, power))
        denominator += math.pow(1.2, power)
    if denominator > 0:
        return numerator / denominator
    return 0

for filename in subDirFiles:
    tensorInputs = []
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
        listOfHandles.append(line[0:len(line) - 2])

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
                print(i)
                for tweet in user_tweets:
                    # append the content of the tweet to 'tweet_contents' variable
                    tweet_contents.append(tweet.text)
                    # append the date of the tweet to 'tweet_dates' varable
                    tweet_dates.append(tweet.created_at)
                    # keep track of what tweet we are on by id
                    last_tweet_id = tweet.id
                # set the next tweets to parse through by making the
                user_tweets = api.user_timeline(screen_name=handle, max_id=last_tweet_id-1, count=200, include_rts=False, trim_user=True, exlude_replies=True)
            # create a Tweet object using the tweet contents and datetime object and append it to tweets
            print("reached this for loop")
            for i in range(0,len(tweet_contents)):
                oldListOfTweets.append(Tweet(tweet_contents[i], tweet_dates[i]))
            listOfTweets = list(filter(isRelevant, oldListOfTweets))
            # perform sentiment analysis on each of the relevant tweets
            for tweet in listOfTweets:
                score = analyze(tweet.getText(), classifier)
                sentiment_scores.append((score, tweet.getDate()))
            tensorInputs.append(weightedScore(sentiment_scores))
            print("refined list of tweets for this handle")
            #sentiment analysis

        except tweepy.error.TweepError:
            print("EEEERRRROOOORRRRR")
            tensorInputs.append(0)
            pass

    if(int(filename[1:2]) <= 5):
        expected = 1
    else:
        expected = 0

    if(INTRODUCTION_DATE < datetime(2017, 1, 3)):
        tensorInputs2014.append([tensorInputs, expected])
    else:
        tensorInputs2016.append([tensorInputs, expected])

    # Add weighted sentiment score for each stream to the list of tensor inputs

#    getJSON from Twitter
#    parse JSON into list of up to 3200 Tweet objects
#    filter by keyword and date
#    get sentiment analysis score for this handle based on remaining tweets
#    add this scaled score to the list of inputs to tensorFlow
#
#run tensorFlow to get prediction probability
