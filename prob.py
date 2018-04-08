import sys
import collections
import os
import string
import nltk
'''
Read's each line and obtains the words, separated by spaces and
places in dictionary (wordcount).
Case and punctuation are distinct. (Should I remove?)
Also how to stratify? All fake together? Separate by pos/neg? Probably test both.
'''
translator = str.maketrans('', '', string.punctuation)

'''
Combines all fake reviews and gets word counts

 or word_tag[0][1] == "NNPS" or word_tag[0][1] == "RB" or word_tag[0][1] == "RBR" or word_tag[0][1] == "RBS" or word_tag[0][1] == "VB" or word_tag[0][1] == "VBD" or word_tag[0][1] == "VBG" or word_tag[0][1] == "VBN" or word_tag[0][1] == "VBZ"
'''
wordsFake = collections.Counter()
wordsNegFake = collections.Counter()
wordsPosFake = collections.Counter()

wordsReal = collections.Counter()
wordsPosReal = collections.Counter()
wordsNegReal = collections.Counter()

wordsFakeCount = 0
wordsNegFakeCount = 0
wordsPosFakeCount = 0

wordsRealCount = 0
wordsPosRealCount = 0
wordsNegRealCount = 0

numberOfFakeReviews = 0
numberOfNegFakeReviews = 0
numberOfPosFakeReviews = 0

numberOfRealReviews = 0
numberOfNegRealReviews = 0
numberOfPosRealReviews = 0

exclaimFake = 0
exclaimNegFake = 0
exclaimPosFake = 0

exclaimReal = 0
exclaimNegReal = 0
exclaimPosReal = 0

#Negative fake
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/negative_polarity/deceptive_from_MTurk/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            numberOfNegFakeReviews = numberOfNegFakeReviews + 1
            numberOfFakeReviews = numberOfFakeReviews + 1
            for line in f:
                for word in line.split():
                    wordsFakeCount = wordsFakeCount + 1
                    wordsNegFakeCount = wordsNegFakeCount + 1
                    word_token = nltk.word_tokenize(word)
                    word_tag = nltk.pos_tag(word_token)
                    if word_tag[0][1] == "JJ" or word_tag[0][1] == "JJR" or word_tag[0][1] == "JJS":
                        wordsFake[word.translate(translator).lower()] += 1
                        wordsNegFake[word.translate(translator).lower()] += 1
                    if "!" in word:
                        exclaimFake = exclaimFake + 1
                        exclaimNegFake = exclaimNegFake + 1

#Positive fake
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/positive_polarity/deceptive_from_MTurk/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            numberOfPosFakeReviews = numberOfPosFakeReviews + 1
            numberOfFakeReviews = numberOfFakeReviews + 1
            for line in f:
                for word in line.split():
                    wordsFakeCount = wordsFakeCount + 1
                    wordsPosFakeCount = wordsPosFakeCount + 1
                    word_token = nltk.word_tokenize(word)
                    word_tag = nltk.pos_tag(word_token)
                    if word_tag[0][1] == "JJ" or word_tag[0][1] == "JJR" or word_tag[0][1] == "JJS":
                        wordsFake[word.translate(translator).lower()] += 1
                        wordsPosFake[word.translate(translator).lower()] += 1
                    if "!" in word:
                        exclaimFake = exclaimFake + 1
                        exclaimPosFake = exclaimPosFake + 1


#Negative real
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/negative_polarity/truthful_from_Web/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            numberOfNegRealReviews = numberOfNegRealReviews + 1
            numberOfRealReviews = numberOfRealReviews + 1
            for line in f:
                for word in line.split():
                    wordsRealCount = wordsRealCount + 1
                    wordsNegRealCount = wordsNegRealCount + 1
                    word_token = nltk.word_tokenize(word)
                    word_tag = nltk.pos_tag(word_token)
                    if word_tag[0][1] == "JJ" or word_tag[0][1] == "JJR" or word_tag[0][1] == "JJS":
                        wordsReal[word.translate(translator).lower()] += 1
                        wordsNegReal[word.translate(translator).lower()] += 1
                    if "!" in word:
                        exclaimReal = exclaimReal + 1
                        exclaimNegReal = exclaimNegReal + 1

#Positive real
for i in range (1,6):
    path = "op_spam_v1.4/op_spam_v1.4/positive_polarity/truthful_from_TripAdvisor/fold" + str(i) + "/"
    for filename in os.listdir(path):
        with open(path + filename,"r") as f:
            #print(path + filename)
            numberOfPosRealReviews = numberOfPosRealReviews + 1
            numberOfRealReviews = numberOfRealReviews + 1
            for line in f:
                for word in line.split():
                    wordsPosRealCount = wordsPosRealCount + 1
                    wordsRealCount = wordsRealCount + 1
                    word_token = nltk.word_tokenize(word)
                    word_tag = nltk.pos_tag(word_token)
                    if word_tag[0][1] == "JJ" or word_tag[0][1] == "JJR" or word_tag[0][1] == "JJS":
                        wordsReal[word.translate(translator).lower()] += 1
                        wordsPosReal[word.translate(translator).lower()] += 1
                    if "!" in word:
                        exclaimReal = exclaimReal + 1
                        exclaimPosReal = exclaimPosReal + 1



print("Most common words in Fake reviews:")
print(collections.Counter(wordsFake).most_common(10))
print("Average word count in Fake reviews:")
print(wordsFakeCount/numberOfFakeReviews)
print("Average exclaimation point in Fake reviews:")
print(exclaimFake/numberOfFakeReviews)


print("\n Most common words in Negative Fake Reviews")
print(collections.Counter(wordsNegFake).most_common(10))
print("Average word count in Negative Fake reviews:")
print(wordsNegFakeCount/numberOfNegFakeReviews)
print("Average exclaimation point in Negative Fake reviews:")
print(exclaimNegFake/numberOfNegFakeReviews)


print("\n Most common words in Positive Fake Reviews")
print(collections.Counter(wordsPosFake).most_common(10))
print("Average word count in Positive Fake reviews:")
print(wordsPosFakeCount/numberOfPosFakeReviews)
print("Average exclaimation point in Positive Fake reviews:")
print(exclaimPosFake/numberOfPosFakeReviews)


print("\n Most common words in Real Reviews")
print(collections.Counter(wordsReal).most_common(10))
print("Average word count in Real reviews:")
print(wordsRealCount/numberOfRealReviews)
print("Average exclaimation point in Real reviews:")
print(exclaimReal/numberOfRealReviews)


print("\n Most common words in Negtaive Real Reviews")
print(collections.Counter(wordsNegReal).most_common(10))
print("Average word count in Negative Real reviews:")
print(wordsNegRealCount/numberOfNegRealReviews)
print("Average exclaimation point in Negative Real reviews:")
print(exclaimNegReal/numberOfNegRealReviews)


print("\n Most common words in Positive Real Reviews")
print(collections.Counter(wordsPosReal).most_common(10))
print("Average word count in Positive Real reviews:")
print(wordsPosRealCount/numberOfPosRealReviews)
print("Average exclaimation point in Positive Real reviews:")
print(exclaimPosReal/numberOfPosRealReviews)
f.close()
