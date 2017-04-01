import requests
from bs4 import BeautifulSoup

def get_bill_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.find(id = "billTextContainer").get_text()
    return text

def get_bill_date(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    date = soup.find("h1", {"class":"legDetail"}).find('span').get_text()
    return date

def get_bill_name(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    whole_title = soup.find("h1", {"class":"legDetail"}).get_text()
    date = soup.find("h1", {"class":"legDetail"}).find('span').get_text()
    title = whole_title.replace("date", '')
    return title