import sys
import collections
import os
import string

'''
Read's each line and obtains the words, separated by spaces and
places in dictionary (wordcount).
Case and punctuation are distinct. (Should I remove?)
Also how to stratify? All fake together? Separate by pos/neg? Probably test both.
'''
translator = str.maketrans('', '', string.punctuation)

'''
Combines all fake reviews and gets word counts
'''
wordsFake = collections.Counter()
wordsNegFake = collections.Counter()
wordsPosFake = collections.Counter()

wordsReal = collections.Counter()
wordsPosReal = collections.Counter()
wordsNegReal = collections.Counter()

#Negative fake
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/negative_polarity/deceptive_from_MTurk/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            for line in f:
                for word in line.split():
                    wordsFake[word.translate(translator).lower()] += 1
                    wordsNegFake[word.translate(translator).lower()] += 1
#Positive fake
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/positive_polarity/deceptive_from_MTurk/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            for line in f:
                for word in line.split():
                    wordsFake[word.translate(translator).lower()] += 1
                    wordsPosFake[word.translate(translator).lower()] += 1

#Negative real
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/negative_polarity/truthful_from_Web/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            for line in f:
                for word in line.split():
                    wordsReal[word.translate(translator).lower()] += 1
                    wordsNegReal[word.translate(translator).lower()] += 1
#Positive fake
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/positive_polarity/truthful_from_TripAdvisor/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            for line in f:
                for word in line.split():
                    wordsReal[word.translate(translator).lower()] += 1
                    wordsPosReal[word.translate(translator).lower()] += 1



print(collections.Counter(wordsFake).most_common(10))
print(collections.Counter(wordsNegFake).most_common(10))
print(collections.Counter(wordsPosFake).most_common(10))
print(collections.Counter(wordsReal).most_common(10))
print(collections.Counter(wordsNegReal).most_common(10))
print(collections.Counter(wordsPosReal).most_common(10))
f.close()
