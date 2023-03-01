from datetime import datetime
from bs4 import BeautifulSoup
import json


def gettime(article):
    p_date_with_tz = article.publish_date
    p_date_without_tz = None
    iso_formatted = None
    if p_date_with_tz:
        p_date_without_tz = p_date_with_tz.replace(tzinfo=None)
        print('p_date_with_tz yes')
    
    if not p_date_without_tz:
        soup = BeautifulSoup(article.html, 'html.parser')
        time_tag = soup.find('time')
        print('p_date_without_tz no')
        if time_tag:
            pub_date = time_tag.text.strip()
            print('time_tag yes')
            p_date_without_tz = datetime.strptime(pub_date, '%d %B,%Y %I:%M %p')

    if not p_date_without_tz:
        soup = BeautifulSoup(article.html, 'html.parser')
        bbc_dictionary = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))

        date_published = [value for (key, value) in bbc_dictionary.items() if key == 'datePublished']
        print('p_date_without_tz no')
        # converting into standard format
        if date_published:
            date_obj = datetime.strptime(date_published[0], '%Y-%m-%dT%H:%M:%S%z')
            print('date_published yes')
            p_date_without_tz =  date_obj.replace(tzinfo= None)

    if p_date_without_tz:
        iso_formatted = p_date_without_tz.isoformat()
        print('p_date_with_tz yes')
    return iso_formatted





# def gettime(article):
#     p_date_with_tz = article.publish_date
#     p_date_without_tz = None
#     iso_formatted = None
#     if p_date_with_tz:
#         p_date_without_tz = p_date_with_tz.replace(tzinfo=None)
    
#     if not p_date_without_tz:
#         soup = BeautifulSoup(article.html, 'html.parser')
#         time_tag = soup.find('time')
        
#         if time_tag:
#             pub_date = time_tag.text.strip()
#             p_date_without_tz = datetime.strptime(pub_date, '%d %B,%Y %I:%M %p')

#     if not p_date_without_tz:
#         soup = BeautifulSoup(article.html, 'html.parser')
#         bbc_dictionary = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))

#         date_published = [value for (key, value) in bbc_dictionary.items() if key == 'datePublished']

#         # converting into standard format
#         if date_published:
#             date_obj = datetime.strptime(date_published[0], '%Y-%m-%dT%H:%M:%S%z')
#             p_date_without_tz =  date_obj.replace(tzinfo= None)

#         if p_date_with_tz:
#             iso_formatted = p_date_without_tz.isoformat()

#         return iso_formatted

