import csv

def parse_csv(data_file):
    # given a csv file containing sentiment data, returns a list of tuples containing the text and the sentiment
    # r = requests.get(data_file)
    # text = r.iter_lines(decode_unicode=True)
    data_list = []

    with open(data_file, 'r', encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                if row['Sentiment'] == '0':
                    sentiment = 'negative'
                else:
                    sentiment = 'positive'

                pair = (row['SentimentText'].strip(), sentiment)
                data_list.append(pair)
            except:
                pass

    return data_list

def splitTrainingTweets(training_tweets):
    split_tweets = []
    for (words, sentiment) in training_tweets:
        words_filtered = [x.lower() for x in words.split() if len(x) >= 3]
        split_tweets.append((words_filtered, sentiment))
    return split_tweets

