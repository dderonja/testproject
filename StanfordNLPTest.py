import pandas as pd
from pycorenlp import StanfordCoreNLP
from googletrans import Translator



host = "http://localhost"
port = "9000"
nlp = StanfordCoreNLP(host + ":" + port)

df = pd.read_csv('csvs/output/reweChecked.csv', delimiter=',', encoding='utf-8')
counter = 0
counter_right = 0
for idx, row in df.iterrows():
    counter = counter + 1
    print(counter)
    category = df.loc[idx, 'Kategorie']
    if counter > 1500:
        break
    if pd.notnull(df.loc[idx, 'Nachricht']) and df.loc[idx, 'Projektergebnis'] != 'Englisch' and df.loc[idx, 'Projektergebnis'] != 'Werbung' and df.loc[idx, 'Projektergebnis'] != 'Only Link':
        text = df.loc[idx, 'Nachricht']

        output = nlp.annotate(
            text,
            properties={
                "outputFormat": "json",
                "annotators": "sentiment"
            }
        )

        # json = json.loads(output)
        sentiment = output[output.index('sentiment":') + 13:output.index('sentiment":') + 20]


        if sentiment == 'Negativ':
            sentiment = 'negativ '
            df.loc[idx, 'Projektergebnis'] = sentiment
        if sentiment == 'Positiv':
            sentiment = 'positiv '
        if sentiment == 'Neutral':
            sentiment = 'neutral '

        if sentiment == df.loc[idx, 'Kategorie']:

            counter_right = counter_right + 1





print(counter_right)
print(counter)
df.to_csv("csvs/output/rewePolarity.csv", encoding='utf-8', sep=',', index=False)
