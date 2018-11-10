import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    iam_apikey='jToftXptzDKXcTKUm2zWY1E_ZjrZTYiAHI4xMkCR97CX',
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api'
)

def get_label(text):
    try:
        response = natural_language_understanding.analyze(
        text=text,
        features=Features(sentiment=SentimentOptions())).get_result()

        return response['sentiment']['document']['label']

    except:
        return 'neutral'
    
myfile = open("dataset.txt", "r")
positive_file = open("p.txt", "w")
negative_file = open("n.txt", "w")
lines = myfile.readlines()
i = 0
for line in lines:    
    if(get_label(line) == 'positive'):
        positive_file.write(line)
        positive_file.flush()
    elif(get_label(line) == 'negative'):
        negative_file.write(line)
        negative_file.flush()
    i+=1
    print(i)
