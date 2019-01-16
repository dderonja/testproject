from nltk.stem.snowball import *
stemmer = SnowballStemmer("german")


text = 'spielen spielt'
text = text.split()
print(text)
stemmed = [stemmer.stem(i) for i in text]
print(stemmed)