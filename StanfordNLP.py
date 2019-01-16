
import json
from pycorenlp import StanfordCoreNLP
from googletrans import Translator
from textblob import TextBlob
host = "http://localhost"
port = "9000"
nlp = StanfordCoreNLP(host + ":" + port)
text = 'test'
test = TextBlob(text)

print(text)
output = nlp.annotate(
    test.string,
    properties={
        "outputFormat": "json",
        "annotators": "sentiment"
    }
)

#json = json.loads(output)
sentiment = output[output.index('sentiment":')+13:output.index('sentiment":')+20]
print(sentiment)


