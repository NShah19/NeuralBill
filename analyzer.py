import nltk

def get_words_in_tweets (tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features


def set_training_set (word_features, training_tweets):

	def extract_features(document):
		document_words = set(document)
		features = {}
		for word in word_features:
			features['contains(%s)' % word] = (word in document_words)
		return features

	return nltk.classify.apply_features(extract_features, training_tweets)

def analyze (tweet, classifier):
	if classifier.classify(extract_features(tweet.split())) == "positive":
		return 1
	return -1

def get_classifier (training_set):
	classifier = nltk.NaiveBayesClassifier.train(training_set)
	return classifier
