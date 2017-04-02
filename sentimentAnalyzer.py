import nltk
from trainingTweets import training_tweets

def process(tweets):
    # Given a lists of messages, splits the messages and deletes words with length less than 3.
    processed_tweets = []
    for (words, sentiment) in tweets:
        words_filtered = [x.lower() for x in words.split() if len(x) >= 3]
        processed_tweets.append((words_filtered, sentiment))
    print("Test 2")
    return processed_tweets

def get_word_features(processed_tweets):
    # Given a list of processed messages, returns a list with words in order of freuqency.
    all_words = []
    for (words, sentiment) in processed_tweets:
        all_words.extend(words)

    word_list = nltk.FreqDist(all_words)
    word_features = word_list.keys()
    return word_features

def extract_features(document):
    # Given a list of strings, returns a dictionary indicating what words are contained in the input passed.
    word_features = get_word_features(process(training_tweets))
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def get_classifier(tweets):
    # Takes in training data in the form of a tuple containing a message and whether it is positive or negative and returns a classifier.
    processed_tweets = process(tweets)
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