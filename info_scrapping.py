import requests
from bs4 import BeautifulSoup 

url = 'https://en.wikipedia.org/wiki/Apple_Inc.'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def getName(url):
    company_name = soup.find('h1', id='firstHeading')
    company_name = company_name.text

    return company_name

def getDescription(url):
    container = soup.find('div',id='bodyContent')
    box = container.find('div', id='mw-content-text')
    contents = box.find("div", class_="mw-parser-output")

    return contents

def getShortDescr(contents):
    short_descr = contents.find("div")
    short_descr = short_descr.text

    return short_descr 

def getLongDescr(contents):
    paragraphs = contents.find_all("p")
    long_descr = paragraphs[1].text

    return long_descr


company_name = getName(url)
contents = getDescription(url)
short_descr = getShortDescr(contents)
long_descr = getLongDescr(contents)

print(company_name)
print("short descr: "+ short_descr)
print("long descr: "+ long_descr)

