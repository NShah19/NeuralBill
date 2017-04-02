import nltk
from trainingTweets import training_tweets

def get_words_in_tweets(data_tweets):
    # Given a lists of messages, splits the messages and deletes words with length less than 3 letters.
    processed_tweets = []
    for (words, sentiment) in data_tweets:
        words_filtered = [x.lower() for x in words.split() if len(x) >= 3]
        processed_tweets.append((words_filtered, sentiment))
    return processed_tweets

def get_word_features(word_list):
    # Given a list of processed messages, returns a list with words in order of freuqency.
    word_list = nltk.FreqDist(word_list)
    word_features = word_list.keys()
    print(word_list)
    return word_features

def extract_features(document):
    # Given a list of strings, returns a dictionary indicating what words are contained in the input passed.
    word_features = get_word_features(get_words_in_tweets(training_tweets))

    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def get_classifier(data_tweets):
    # Takes in training data in the form of a tuple containing a message and whether it is positive or negative and returns a classifier.
    processed_tweets = get_words_in_tweets(data_tweets)
    training_set = nltk.classify.apply_features(extract_features, processed_tweets)
    print("Done training set")
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Done with classifier")
    return classifier

def analyze(tweet, classifier):
    # Takes in a message and a classifier and returns whether the classifier thinks it is positive or negative. If it is positive, returns 1. If it is negative, returns -1.
    if classifier.classify(extract_features(tweet.split())) == "positive":
        return 1
    return -1
