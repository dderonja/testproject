
import json
from pycorenlp import StanfordCoreNLP
host = "http://localhost"
port = "9000"
nlp = StanfordCoreNLP(host + ":" + port)
text = "das sind überragende neuigkeiten"
output = nlp.annotate(
    text,
    properties={
        "outputFormat": "json",
        "annotators": "sentiment"
    }
)

#json = json.loads(output)
sentiment = output[output.index('sentiment":')+13:output.index('sentiment":')+20]
print(sentiment)


