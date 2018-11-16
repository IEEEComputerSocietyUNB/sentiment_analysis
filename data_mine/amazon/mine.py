from threading import Thread
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

def mine(lines, thread_range, my_files):    
    print("Starting process")
    for i in thread_range:
        # print("Step", i)
        line = lines[i]
        try:
            if(detect(line) == 'en'):
                if(line.find('__label__1 ') != -1):
                    line = line.replace('__label__1 ','')    
                    clean = remove_stopwords(clean_line(line))
                    my_files[0].write(clean)

                elif(line.find('__label__2 ') != -1):
                    line = line.replace('__label__2 ','')    
                    clean = remove_stopwords(clean_line(line))
                    my_files[1].write(clean)        
        except:            
            continue

    my_files[0].close()
    my_files[1].close()
    print("Process finalized")    


def tt(lines, thread_range, my_files):
    for i in thread_range:
        my_files[0].write(str(i) + '\n')
        my_files[1].write(str(i) + '\n')

    my_files[0].close()
    my_files[1].close()

myfile   = open("data_mine/amazon/data.txt", "r")
pos_file = [open('data_mine/amazon/p0.txt', 'w'), open('data_mine/amazon/p1.txt', 'w'), open('data_mine/amazon/p2.txt', 'w')]
neg_file = [open('data_mine/amazon/n0.txt', 'w'), open('data_mine/amazon/n1.txt', 'w'), open('data_mine/amazon/n2.txt', 'w')]
lines = myfile.readlines()

before = datetime.now()

range_size  = 133333
upper_range = 133333
threads = []
for i in range(0,3):
    this_range = range(upper_range - range_size, upper_range)

    upper_range += range_size
    files = [pos_file[i], neg_file[i]]
    t = Thread(target=mine, args=(lines, this_range,files,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('All threads returned, took exactly:')
print((datetime.now() - before))