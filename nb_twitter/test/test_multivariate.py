# -*- coding: utf-8 -*-

# test_multivariate.py
# nb_twitter/nb_twitter/bayes
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-29
# Modified.........................2015-06-29
#
# This script was developed for use as part of the nb_twitter package


from nb_twitter.bayes import multivariate


train_class = ['c', 'j']

train_docs = [['c', 'chinese beijing chinese'],
              ['c', 'chinese chinese shanghai'],
              ['c', 'chinese macao'],
              ['j', 'tokyo japan chinese']]

test_docs = 'chinese chinese chinese tokyo japan'

classifier = multivariate.Multivariate(train_class, train_docs)

classifier.train()
results = classifier.run(test_docs)

print "C\t\t=", classifier.C
print "D\t\t=", classifier.D
print "N\t\t=", classifier.N
print "V\t\t=", classifier.V
print "Nc\t\t=", classifier.Nc
print "Prior\t=", classifier.prior
print "Prob\t=", classifier.prob
print
print(results)