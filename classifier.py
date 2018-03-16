from sklearn import svm
import random
'''
Used to read in X matrix (data set).
'''
with open("./spambase/spambase.data", 'r') as fobj:
    X = [[float(num) for num in line.split(',')] for line in fobj]

random.shuffle(X)
'''
Used to read in Y vector (attribute names).
'''
y = []
for row in X:
    y.append(row[len(row)-1])


'''
We're going to stratify X in containing only word freq, char freq, capital freq
and compare the different accuracy rates and false positivies using these prediction
models.
'''


wordX = []
for row in X:
    wordX.append(row[:48])

clfWord = svm.SVC()
clfWord.fit(wordX[0:4000], y[0:4000])
testWordX = clfWord.predict(wordX[4000:])

countWord = 0
countWordFalse = 0
for i in range(len(testWordX)):
    if testWordX[i] == y[4000+i]:
        countWord = countWord + 1
    if testWordX[i] == 1 and y[4000+i] == 0:
        countWordFalse = countWordFalse + 1

print("Words:")
print("Percent spam = " + str(countWord/len(y[4000:])))
print("Percent false positive = " + str(countWordFalse/len(y[4000:])))
print()
#-------------------------------------------------------
charX = []
for row in X:
    charX.append(row[48:54])

clfChar = svm.SVC()
clfChar.fit(charX[0:4000], y[0:4000])
testCharX = clfChar.predict(charX[4000:])

countChar = 0
countCharFalse = 0
for i in range(len(testCharX)):
    if testCharX[i] == y[4000+i]:
        countChar = countChar + 1
    if testCharX[i] == 1 and y[4000+i] == 0:
        countCharFalse = countCharFalse + 1
print("Chars:")
print("Percent spam = " + str(countChar/len(y[4000:])))
print("Percent false positive = " + str(countCharFalse/len(y[4000:])))
print()

#-----------------------------------------------------
capX = []
for row in X:
    capX.append(row[54:])

clfCap = svm.SVC()
clfCap.fit(capX[0:4000], y[0:4000])
testCapX = clfCap.predict(capX[4000:])

countCap = 0
countCapFalse = 0
for i in range(len(testCapX)):
    if testCapX[i] == y[4000+i]:
        countCap = countCap + 1
    if testCapX[i] == 1 and y[4000+i] == 0:
        countCapFalse = countCapFalse + 1
print("Capital:")
print("Percent spam = " + str(countCap/len(y[4000:])))
print("Percent false positive = " + str(countCapFalse/len(y[4000:])))
print()

#-----------------------------------------------------
'''
All attributes
'''

clf = svm.SVC()
clf.fit(X[0:4000], y[0:4000])
testX = clf.predict(X[4000:])


count = 0
countFalse = 0
for i in range(len(testX)):
    if testX[i] == y[4000+i]:
        count = count + 1
    if testX[i] == 1 and y[4000+i] == 0:
        countFalse = countFalse + 1
print("Total:")
print("Percent spam = " + str(count/len(y[4000:])))
print("Percent false positive = " + str(countFalse/len(y[4000:])))
print()
