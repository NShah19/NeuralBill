# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.
import urllib.request, urllib.error, urllib.parse
import sys
import base64
import json
from api_keys import account_key
from parse_bill import get_bill_text

# Azure portal URL.
base_url = 'https://westus.api.cognitive.microsoft.com/'
# Your account key goes here.
# account_key = '<your account key>'

headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}


# input_texts = '{"documents":[{"id":"1","text":"hello world"},{"id":"2","text":"hello foo world"},{"id":"three","text":"hello my world"},]}'

url = 'https://www.congress.gov/bill/114th-congress/house-bill/1321/text'
input_texts = '{"documents":[{"id":"1","text":"%s"},]}' % (get_bill_text(url))

# Detect key phrases.
batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
req = urllib.request.Request(batch_keyphrase_url, input_texts.encode('utf-8'), headers)
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
obj = json.loads(result)
for keyphrase_analysis in obj['documents']:
    print(('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases']))))

# Detect language.
# num_detect_langs = 1;
# language_detection_url = base_url + 'text/analytics/v2.0/languages' + ('?numberOfLanguagesToDetect=' + num_detect_langs if num_detect_langs > 1 else '')
# req = urllib.request.Request(language_detection_url, input_texts, headers)
# response = urllib.request.urlopen(req)
# result = response.read()
# obj = json.loads(result)
# for language in obj['documents']:
#     print(('Languages: ' + str(language['id']) + ': ' + ','.join([lang['name'] for lang in language['detectedLanguages']])))

# Detect sentiment.
# batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
# req = urllib.request.Request(batch_sentiment_url, input_texts, headers)
# response = urllib.request.urlopen(req)
# result = response.read()
# obj = json.loads(result)
# for sentiment_analysis in obj['documents']:
#     print(('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score'])))
