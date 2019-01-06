import pandas as pd

df = pd.read_csv('csvs/output/rewe.csv', delimiter=',', encoding='iso-8859-1')
# Entfernen von nicht benötigten Attributen
df.drop('Erstellungsdatum', axis=1, inplace=True)
df.drop('Name des Kanals', axis=1, inplace=True)
df.drop('Typ', axis=1, inplace=True)
df.drop('Name des Autors', axis=1, inplace=True)
df.drop('Profil des Autors', axis=1, inplace=True)
df.drop('URL', axis=1, inplace=True)
df.rename(columns={'Nachricht': 'text'})

df.to_csv("csvs/output/reweAnca.csv", encoding='iso-8859-1', sep=',', index=False)

# Stopwords rausschmeißen
#   stop_words = (lex for lex in nlp.vocab if lex.is_stop)
# if token.is_stop:
# entferne Stopwords