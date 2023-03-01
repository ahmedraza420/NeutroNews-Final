from datetime import datetime
from bs4 import BeautifulSoup
import json


def gettime(article):
    p_date_with_tz = article.publish_date
    p_date_without_tz = None
    if p_date_with_tz:
        p_date_without_tz = p_date_with_tz.replace(tzinfo=None)
    
    if not p_date_without_tz:
        soup = BeautifulSoup(article.html, 'html.parser')
        time_tag = soup.find('time')
        pub_date = time_tag.text.strip()
        if pub_date:
            p_date_without_tz = datetime.strptime(pub_date, '%d %B,%Y %I:%M %p')

    if not p_date_without_tz:
        soup = BeautifulSoup(article.html, 'html.parser')
        bbc_dictionary = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))

        date_published = [value for (key, value) in bbc_dictionary.items() if key == 'datePublished']

        # converting into standard format
        if date_published:
            date_obj = datetime.strptime(date_published[0], '%Y-%m-%dT%H:%M:%S%z')
            p_date_without_tz =  date_obj.replace(tzinfo= None)

    return p_date_without_tz

