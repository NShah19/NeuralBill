import urllib.request, urllib.error, urllib.parse
import sys
import base64
import json
from api_keys import account_key

base_url = 'https://westus.api.cognitive.microsoft.com/'
headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}

url = 'https://www.congress.gov/bill/114th-congress/house-bill/1321/text'

input_texts = '{"documents":[{"id":"1","text":"hello world"},{"id":"2","text":"hello foo world"},{"id":"three","text":"hello my world"},]}'

# Detect sentiment.
batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
req = urllib.request.Request(batch_sentiment_url, input_texts.encode('utf-8'), headers)
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
obj = json.loads(result)
for sentiment_analysis in obj['documents']:
    print(('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score'])))
