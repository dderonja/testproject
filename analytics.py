#https://www.analyticsvidhya.com/blog/2018/07/hands-on-sentiment-analysis-dataset-python/
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
from nltk.stem.snowball import *
stemmer = SnowballStemmer("german")
warnings.filterwarnings("ignore", category=DeprecationWarning)

combi = pd.read_csv('csvs/output/reweCleanRows.csv', delimiter=',',encoding='utf-8')
combi['Nachricht'] = combi['Nachricht'].astype(str)
combi['Nachricht'] = combi['Nachricht'].str.replace("[^a-zA-Z#]", " ")
combi['Nachricht'] = combi['Nachricht'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
tokenized_tweet = combi['Nachricht'].apply(lambda x: x.split())
tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x])

for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

combi['Nachricht'] = tokenized_tweet
print(combi.head())

tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(combi['Nachricht'][combi['Kategorie'] == 'negativ'])
print(tfidf)
all_words = ' '.join([text for text in combi['Nachricht'][combi['Kategorie'] == 'negativ']])
wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()

