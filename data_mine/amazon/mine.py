from langdetect import detect
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean_line(string):
    ret_string = ""
    for char in string:        
        if(char.isalpha() or char.isspace()):            
            ret_string += char

    ret_string = ' '.join(ret_string.split())
    return ret_string.lower()

def remove_stopwords(string):
    tokens = word_tokenize(string)
    filtered_sentence = [word for word in tokens if word not in stopwords.words("english")]
    return ' '.join(filtered_sentence) + '\n'


myfile   = open("data_mine/amazon/data.txt", "r")
pos_file = open('data_mine/amazon/p.txt', 'w')
neg_file = open('data_mine/amazon/n.txt', 'w')
lines = myfile.readlines()

before = datetime.now()
print("Starting process")
for i in range(0,4000):
    print("Step", i)
    line = lines[i]
    if(detect(line) == 'en'):
        if(line.find('__label__1 ') != -1):
            line = line.replace('__label__1 ','')    
            clean = remove_stopwords(clean_line(line))
            neg_file.write(clean)

        elif(line.find('__label__2 ') != -1):
            line = line.replace('__label__2 ','')    
            clean = remove_stopwords(clean_line(line))
            pos_file.write(clean)
print("Process finalized")
print((datetime.now() - before)*100)            
