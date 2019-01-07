from textblob_de import TextBlobDE
import pandas as pd
import re

df = pd.read_csv('csvs/output/reweChecked.csv', delimiter=',', encoding='iso-8859-1')
counter = 0
counter_right = 0
for idx, row in df.iterrows():
    counter = counter + 1
    category = df.loc[idx, 'Kategorie']
    if counter > 5000:
        break
    if pd.notnull(df.loc[idx, 'Nachricht']) and df.loc[idx, 'Projektergebnis'] != 'Englisch' and df.loc[idx, 'Projektergebnis'] != 'Werbung' and df.loc[idx, 'Projektergebnis'] != 'Only Link':

        text = df.loc[idx, 'Nachricht']
        test = TextBlobDE(text)
        polarity = test.sentiment.polarity


        if polarity > 0.5:
            df.loc[idx, 'Projektergebnis'] = 'positiv '
            sentiment = 'positiv '
        elif polarity < -0.3:
            df.loc[idx, 'Projektergebnis'] = 'negativ '
            sentiment = 'negativ '
        else:
            df.loc[idx, 'Projektergebnis'] = 'neutral '
            sentiment = 'neutral '

    else:
        df.loc[idx, 'Projektergebnis'] = 'neutral '
        sentiment = 'neutral '

    if sentiment == category:
        counter_right = counter_right + 1

print(counter_right)
print(counter)
# df.to_csv("csvs/output/reweChecked.csv", encoding='iso-8859-1', sep=',', index=False)
