# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.
import urllib.request, urllib.error, urllib.parse
import sys
import base64
import json
import csv
from time import sleep
from random import shuffle
from api_keys import account_key
from parse_bill import get_bill_text, get_bill_start_date, get_bill_end_date, get_bill_name
import operator

# Azure portal URL.
base_url = 'https://westus.api.cognitive.microsoft.com/'
# Your account key goes here.
# account_key = '<your account key>'
headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}


# url = 'https://www.congress.gov/bill/114th-congress/house-bill/2029/text'
# url = 'https://www.congress.gov/bill/114th-congress/house-bill/1321/text'

def get_key_phrases(url):
    full_text = get_bill_text(url)
    list_full_text = full_text.split()
    result_list = [] # result list to store each 50000 new string
    maxwords = 500
    for i in range(0, (len(list_full_text)//maxwords) + 1):
        result_list.append(' '.join(list_full_text[i*maxwords:min((i+1) * maxwords, len(list_full_text))]))

    shuffle(result_list)
    input_texts = []
    for i in range(0, len(result_list)):
        input_texts.append('{"documents":[{"id":"%s","text":"%s"},]}' % (str(i+1), result_list[i]))
    print(len(input_texts))

    # Detect key phrases.
    batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
    keyword_dict = {}
    for i in range(0, 95):
        print(i)
        req = urllib.request.Request(batch_keyphrase_url, input_texts[i].encode('utf-8'), headers)
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        obj = json.loads(result)
        keyphrase_analysis = obj['documents'][0]['keyPhrases']
        for j in range(len(keyphrase_analysis)):
            target = keyword_dict.get(keyphrase_analysis[j])
            if not target:
                keyword_dict[keyphrase_analysis[j]] = 1
            else:
                keyword_dict[keyphrase_analysis[j]] += 1
    #         print(('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases']))))
    sortedKeywords = sorted(keyword_dict.items(), key = operator.itemgetter(1))
    finalKeywordList = [sortedKeywords[(-1 * i) - 1][0] for i in range(min(500, len(sortedKeywords)))]

    bill_name = get_bill_name(url)
    bill_start_date = get_bill_start_date(url)
    bill_end_date = get_bill_end_date(url)

    csvFile = open(bill_name + '.csv', 'w')
    writer = csv.writer(csvFile)
    writer.writerow([bill_name])
    writer.writerow([bill_start_date])
    writer.writerow([bill_end_date])
    for i in range(len(finalKeywordList)):
        writer.writerow([finalKeywordList[i]])
    csvFile.close()

        # place into a set
    print("Done")
