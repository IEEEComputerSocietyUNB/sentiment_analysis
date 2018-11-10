import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import time

def prepare_dict(line):    
    my_dict = dict([(word, True) for word in line])
    return my_dict

def read_file(my_file, label):
    lines = my_file.readlines()
    arr = []
    for line in lines:
        dic = prepare_dict(word_tokenize(line))
        arr.append((dic, label))
    return arr

positive_file = open("pw.txt", "r")
negative_file = open("nw.txt", "r")

print('building positives...')
pos_quotes = read_file(positive_file, 'positive')
print('building negatives...')
neg_quotes = read_file(negative_file, 'negative')

train_set = neg_quotes[:3400] + pos_quotes[:3400]
test_set  = neg_quotes[-350:] + pos_quotes[-104:]
print(len(train_set), len(test_set))

classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)

test1 = 'i like happy things'
test2 = 'i am depressed'
test3 = 'i will kill myself'
test4 = 'i love myself'

words = word_tokenize(test1)
useful_words = [word for word in words if word not in stopwords.words("english")]
words1 = prepare_dict(useful_words)

words = word_tokenize(test2)
useful_words = [word for word in words if word not in stopwords.words("english")]
words2 = prepare_dict(useful_words)

words = word_tokenize(test3)
useful_words = [word for word in words if word not in stopwords.words("english")]
words3 = prepare_dict(useful_words)

words = word_tokenize(test4)
useful_words = [word for word in words if word not in stopwords.words("english")]
words4 = prepare_dict(useful_words)

print(test1 + ' ' + classifier.classify(words1))
print(test2 + ' ' + classifier.classify(words2))
print(test3 + ' ' + classifier.classify(words3))
print(test4 + ' ' + classifier.classify(words4))
