import pandas as pd
import re
import numpy as np

list_lottery = [
                    ['Gewinnspiel'],
                    ['Umfrage'],
                    ['Zeit nehmen'],
                    ['Werbung'],
                    ['gewinnen'],
                    ['Projekt'],
                    ['']
                ]

df = pd.read_csv('csvs/output/reweAnca.csv', delimiter=',', encoding='iso-8859-1')
counter = 0
for idx, row in df.iterrows():
    counter = counter + 1
    if counter > 20:
        break
    for i in range(0, len(list_lottery)):
        if pd.notnull(df.loc[idx, 'Nachricht']):
            if re.search(list_lottery[i][0], df.loc[idx, 'Nachricht'], re.IGNORECASE):
                df.loc[idx, 'Projektergebnis'] = 'Gewinnspiel'


df.to_csv("csvs/output/reweAnca.csv", encoding='iso-8859-1', sep=',', index=False)
