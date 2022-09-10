import pandas as pd
import spacy
from goose3 import Goose
from textblob import TextBlob

# import nltk
# nltk.download('omw-1.4')
nlp = spacy.load('en_core_web_sm')
# Read list of hundreds of urls from a file
url_list = open("URL.txt", "r").read().split("\n")

# loop for each url
for url in url_list:
    g = Goose()
    article = g.extract(url=url)

# process/store ...
    article.cleaned_text  # cleaning the extracted text
    print(article.cleaned_text) # printing the extracted text
# print(len(article.cleaned_text))  # printing the no of words in articles after article is printed

with open("Output.txt", "w") as external_file:
    print(article.cleaned_text, file=external_file)
    external_file.close()