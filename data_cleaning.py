import pandas as pd

df = pd.read_csv('csvs/input/rewe.csv', delimiter=',', encoding='utf-8')


# Entfernen von nicht benötigten Attributen
df.drop('ID', axis=1, inplace=True)
df.drop('Netzwerk', axis=1, inplace=True)
df.drop('Erstellungsdatum', axis=1, inplace=True)
df.drop('Name des Kanals', axis=1, inplace=True)
df.drop('Typ', axis=1, inplace=True)
df.drop('Name des Autors', axis=1, inplace=True)
df.drop('Profil des Autors', axis=1, inplace=True)
df.drop('URL', axis=1, inplace=True)

# Hinzufügen des Attributes "Projektergebnis"
df.insert(loc=2, column='Projektergebnis', value='')

# Ersetze Umbrüche mit Leerzeichen
df = df.replace('\n', ' ', regex=True)

for idx, row in df.iterrows():
    print(idx)
    # Entferne alle Einträge, die "Null" enthalten
    if pd.isnull(row['Nachricht']):
        df = df[df.index != idx]
        continue
    # Korrigiere die fehlerhaften Sentiment-Strings
    if df.loc[idx, 'Kategorie'] == 'Neutral ' or df.loc[idx, 'Kategorie'] == 'neutral ':
        df.loc[idx, 'Kategorie'] = 'neutral'
        continue
    elif df.loc[idx, 'Kategorie'] == 'Positiv ' or df.loc[idx, 'Kategorie'] == 'positiv ':
        df.loc[idx, 'Kategorie'] = 'positiv'
        continue
    elif df.loc[idx, 'Kategorie'] == 'Negativ ' or df.loc[idx, 'Kategorie'] == 'negativ ':
        df.loc[idx, 'Kategorie'] = 'negativ'
        continue
    elif df.loc[idx, 'Kategorie'] == 'Monitoring ':
        df.loc[idx, 'Kategorie'] = 'neutral'
        continue
    elif df.loc[idx, 'Kategorie'] == 'DSGVO ':
        df.loc[idx, 'Kategorie'] = 'neutral'
        continue
    continue


df.to_csv("csvs/output/reweCleanRows.csv", encoding='utf-8', sep=',', index=False)
