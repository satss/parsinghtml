import requests
from bs4 import BeautifulSoup
import yake
import spacy
from keybert import KeyBERT
from spacy.lang.de.examples import sentences 
nlp = spacy.load("de_core_news_sm")

url = 'https://www.nestle.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
model = KeyBERT('distilbert-base-nli-mean-tokens')




metas = soup.find_all('meta')


for m in metas:
    if m.get ('name') == 'description':
        desc = m.get('content')
        print(desc)
        doc = nlp(desc)
        print(doc.ents)
        keywords = model.extract_keywords(desc)     
        for keyword in keywords:
            print (keyword)

       