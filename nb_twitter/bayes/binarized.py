# -*- coding: utf-8 -*-

# binarized.py
# nb_twitter/nb_twitter/bayes
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-24
# Modified.........................2015-06-26
#
# This script was developed for use as part of the nb_twitter package


import math
from bayes import Bayes
from decorators import string_check


class Binarized (Bayes):
    """This model of Naive Bayes, as described by Dan Jurafsky, is identical to
    the Multinomial Naive Bayes model with only difference that instead of
    measuring all the occurrences of the term t in the document, it measures it
    only once. The reasoning behind this is that the occurrence of the word
    matters more than the word frequency and thus weighting it multiple times
    does not improve the accuracy of the model.

    Both the training and the running algorithms remain the same with only
    exception that instead of using multiple occurrences we clip all word
    counts in each document at 1.

    Multinomial Reference Page:
    http://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html

    Binarized Reference Slides:
    http://www.stanford.edu/class/cs124/lec/sentiment.pptx

    """

    def train(self):
        """This method will train a binarized naive bayes text classifier.
        The classifier will by trained using the provided classes and documents
        from the initializer.

        """

        for c in self.C:
            self.prior[c] = float(self.Nc[c]) / float(self.N)
            concat_text = self.concatenate_class_documents(c)

            sum = 0.0
            count = {}
            for w in self.V:
                self.prob[w] = {}
                count[w] = float(concat_text.count(w))
                count[w] = 1.0 if count[w] >= 1 else 0
                sum += count[w] + 1.0

            for w in self.V:
                self.prob[w][c] = (count[w] + 1.0) / sum
    # end def train

    @string_check
    def run(self, d):
        """This method will run the trained binarized naive bayes text
        classifier. This method will classify the provided document into
        a class.

        :param d: The new document to be classified.

        :return score: A dictionary of scores for this document in each class.

        """

        score = {}

        W = self.extract_words_from_document("binarized", d)

        for c in self.C:
            score[c] = math.log(self.prior[c])
            for w in W:
                score[c] += math.log(self.prob[w][c])

        return score
    # end def run

    @string_check
    def concatenate_class_documents(self, c):
        """This method will concatenate all the words of each document
        belonging to the provided class. This method will append every
        occurrence of a word.

        :param c: The class of training documents to concatenate.

        :return text: A concatenated list of all words belonging to a class.

        """

        text = []

        for d in self.D:
            if d[0] == c:
                text.extend(d[1].split())

        return text
    # end def concatenate_class_documents

# end class Binarized
