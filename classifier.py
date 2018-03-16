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
Train dataset
'''
clf = svm.SVC()
clf.fit(X[0:4000], y[0:4000])
testX = clf.predict(X[4000:])

'''
Compare predicted model and actual values.
'''
count = 0
for i in range(len(testX)):
    if testX[i] == y[4000+1]:
        count = count + 1

print(count/len(y[4000:]))
