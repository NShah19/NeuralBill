from trainingTweets import parse_csv, splitTrainingTweets
from analyzer import get_words_in_tweets, get_word_features, analyze, set_training_set

import pickle
import nltk

# Get Training Tweets
print("\033[1;33;40m Obtaining training data... \033[0m")
training_tweets = parse_csv("TrainingDataset.csv")
training_tweets = training_tweets[:20000]
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
training_set = nltk.classify.apply_features(extract_features, training_tweets)
print("\033[1;32;40m Training set created! \033[0m")

# Create classifier and train!
print("\033[1;33;40m Creating classifier... \033[0m")
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("\033[1;32;40m Classifier created! \033[0m")

f = open('my_classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()