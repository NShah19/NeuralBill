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

    print("Finished parsing csv")
    print(len(data_list))
    return data_list

training_tweets = parse_csv("TrainingDataset.csv")
training_tweets = training_tweets[:100]


