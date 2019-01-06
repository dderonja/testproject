import pandas as pd

df = pd.read_csv('csvs/input/rewe.csv', delimiter=',',encoding='iso-8859-1')

#Hinzufügen des Attributes "Projektergebnis"
df.insert(loc=10, column='Projektergebnis', value='')

#Entfernen von nicht benötigten Attributen
df.drop('ID', axis=1, inplace=True)
df.drop('Netzwerk', axis=1, inplace=True)

df = df.replace('\n','', regex=True)
#Entferne alle Einträge, die "Null" enthalten
for idx, row in df.iterrows():
    if df.loc[idx, 'Nachricht'] == 'Null':
        df.drop(df.loc[idx].index[0], inplace = True)
        continue
    continue


df.to_csv("csvs/output/rewe.csv", encoding='iso-8859-1', sep=',', index=False)