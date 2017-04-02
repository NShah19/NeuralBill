import requests
from bs4 import BeautifulSoup

def get_bill_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.find(id = "billTextContainer").get_text()
    return text

def get_bill_start_date(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    start_date = soup.find("div", {"class":"overview"}).find('td').get_text().split("Introduced ")[1][0:-1]
    return start_date

def get_bill_end_date(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    end_date = soup.find("div", {"class":"overview"}).find_all('tr')[-1].find('td').get_text().split()[0]
    return end_date

def get_bill_name(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    whole_title = soup.find("h1", {"class":"legDetail"}).get_text()
    date = soup.find("h1", {"class":"legDetail"}).find('span').get_text()
    title = whole_title.replace(date, '')
    return title