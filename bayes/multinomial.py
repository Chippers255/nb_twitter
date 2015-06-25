# -*- coding: utf-8 -*-

# multinomial.py
# nb_twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-23
# Modified.........................2015-06-25
#
# This script was developed for use as part of the nb_twitter package


import math
from bayes import Bayes
from decorators import string_check


class Multinomial (Bayes):
    """This model of Naive Bayes, as described by Manning et al (2008),
    estimates the conditional probability of a particular word given a class as
    the relative frequency of word 'w' in documents belonging to class 'c'.

    This variation takes into account the number of occurrences of word 'w' in
    training documents from class 'c', including multiple occurrences.

    """

    def train(self):
        """This method will train a multinomial naive bayes text classifier.
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
                sum += count[w] + 1.0

            for w in self.V:
                self.prob[w][c] = (count[w] + 1.0) / sum
    # end def train

    @string_check
    def run(self, d):
        """This method will run the trained multinomial naive bayes text
        classifier. This method will classify the provided document into
        a class.

        :param d: The new document to be classified.

        :return score: A dictionary of scores for this document in each class.

        """

        score = {}

        W = self.extract_words_from_document(d)

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

# end class Multinomial
