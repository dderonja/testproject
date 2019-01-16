# Some used imports
import pandas as pd
import numpy as np
import os
import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
#https://sigdelta.com/blog/text-analysis-in-pandas/
mpl.rcParams['figure.figsize'] = (8,6)
mpl.rcParams['font.size'] = 12





doc = pd.read_csv('csvs/output/reweCleanRows.csv', delimiter=',',encoding='utf-8')
doc['words'] = doc.Nachricht.str.strip().str.split('[\W_]+')
rows = list()
for row in doc[['Kategorie', 'words']].iterrows():
    r = row[1]
    for word in r.words:
        rows.append((r.Kategorie, word))

words = pd.DataFrame(rows, columns=['Kategorie', 'word'])
words = words[words.word.str.len() > 0]
words['word'] = words.word.str.lower()
counts = words.groupby('Kategorie')\
    .word.value_counts()\
    .to_frame()\
    .rename(columns={'word':'n_w'})

word_sum = counts.groupby(level=0)\
    .sum()\
    .rename(columns={'n_w': 'n_d'})

tf = counts.join(word_sum)

tf['tf'] = tf.n_w/tf.n_d
c_d = words.Kategorie.nunique()

idf = words.groupby('word')\
    .Kategorie\
    .nunique()\
    .to_frame()\
    .rename(columns={'Kategorie':'i_d'})\
    .sort_values('i_d')

idf['idf'] = np.log(c_d/idf.i_d.values)
tf_idf = tf.join(idf)
tf_idf['tf_idf'] = tf_idf.tf * tf_idf.idf
print(tf_idf.head())


print(counts.head())
print(word_sum.head())
print(tf.head())
print(idf.head())

r = tf_idf['tf_idf']\
    .groupby(level=0)\
    .nlargest(10)\
    .reset_index(level=0, drop=True)
r.plot.bar()
plt.show()
