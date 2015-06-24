# -*- coding: utf-8 -*-

# multinomial.py
# nb_twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <>
# Created..........................2015-06-23
# Modified.........................2015-06-24
#
# This script was developed for use as part of the nb_twitter package


import math
import bayes


class Multinomial (bayes.Bayes):
    """This model of Naive Bayes, as described by Manning et al (2008),
    estimates the conditional probability of a particular word given a class as
    the relative frequency of word 'w' in documents belonging to class 'c'.

    This variation takes into account the number of occurrences of word 'w' in
    training documents from class 'c', including multiple occurrences.

    """

    def train (self):
        """

        """

        for c in self.C:
            self.prior[c] = float(self.Nc[c]) / float(self.N)
            concat_text = self.concatenate_class_documents(c)

            sum   = 0.0
            count = {}
            for w in self.V:
                self.prob[w] = {}
                count[w] = float(concat_text.count(w))
                sum     += count[w] + 1.0

            for w in self.V:
                self.prob[w][c] = (count[w] + 1.0) / sum
    # end def train

    def run (self, d):
        """

        :param d:

        :return score:

        """

        score = {}

        W = self.extract_words_from_document(d)

        for c in self.C:
            score[c] = math.log(self.prior[c])
            for w in W:
                score[c] += math.log(self.prob[w][c])

        return score
    # end def run

# end class Multinomial
