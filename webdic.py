# module for lookup word on web dictionary.

import requests
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from bs4.element import Comment
#import urllib2

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


# Initialize unit's argument parser
parser = ArgumentParser()
parser.add_argument("word", help="Word to lookup")


args = parser.parse_args();
    
# Get the word for searching 
word = args.word+"+meaning"

# Compite it into url
url = "https://www.google.com.tw/search?q=" + word

# Get translation into web content. 
webcontent = requests.get("https://www.google.com.tw/search?q=tax+meaning")

# Convert into plain text.
#print(webcontent.text)
#url = "test.html"
#page = urllib2.urlopen(url)
#soup = BeautifulSoup(page.read())

soup = BeautifulSoup(webcontent.text, 'html.parser')
print(webcontent.text)
#print(soup.prettify())
#print(soup.div) 
#divs = soup.find_all("div", {"id":"ires"}, limit=3)
#divs = soup.find_all("div", {"id":"uid_0"}, limit=3)
divs = soup.select('div.kp-blk');
print(divs)
#print(soup.div["ires"])
#print(divs)
div_text = []
#print(type(divs))
for div in divs:
    div_text.append(str(div))

div_soup = BeautifulSoup(str(divs), 'html.parser')
#print(div_text)  
#print (div_soup.prettify())
#print (div_soup.get_text())
#print (div_soup.td)
#tables = div_soup.findAll("table")
#print(div_soup.find_all(["li"]))
 
#texts = soup.findAll(text=True)
#visible_texts = filter(tag_visible, texts)
#print(texts)



   

