from urllib.request import *
from bs4 import BeautifulSoup
import json
import sys

link = sys.argv[1]



def converterHTML(value):
    return value.encode("ascii", "xmlcharrefreplace").decode("utf-8")


def contentExtractor(post):

    title = post.find("h3", {"class": "storytitle"}).text

    title = converterHTML(str(title))
    content = post.findAll("p")

    content = [converterHTML(str(p)) for p in content]

    content = ''.join(content)

    tagListPre = str(post.find("div", {"class":"post_header"}).text).split("|")

    location = tagListPre[1]

    tags = tagListPre[0].split(",") + tagListPre[len(tagListPre)-1].split(",")

    
    

    return {"title": title, "content": content, "location":location, "tags":tags}
    




def extractor(link):
    try:
        html = urlopen(link).read()
    except Exception as e:
        raise e

    soup = BeautifulSoup(html)

    posts = soup.findAll("div", {"class":"post"})
    
    return json.dumps([contentExtractor(post) for post in posts])






        

print(extractor(link))
