import requests
from bs4 import BeautifulSoup

def get_bill_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.find(id = "billTextContainer").get_text()
    return text
