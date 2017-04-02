import csv

def parse_csv(data_file):
    # given a csv file containing sentiment data, returns a list of tuples containing the text and the sentiment
    # r = requests.get(data_file)
    # text = r.iter_lines(decode_unicode=True)
    with open(data_file, 'r', encoding="utf8") as csv_file:
        reader = csv.DictReader(data_file)

        data_list = []

        for row in reader:
            try:
                if row[1] == '0':
                    sentiment = 'negative'
                else:
                    sentiment = 'positive'

                pair = (row[3].strip(), sentiment)
                data_list.append(pair)
            except:
                pass

    print("Finished parsing csv")
    return data_list

training_tweets = parse_csv("TwitterSentiAnalysisDataset.csv")
print("Test")