# -*- coding: utf-8 -*-

# multivariate.py
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


class Multivariate (bayes.Bayes):
    """

    """

    def train (self):
        """

        """

        for c in self.C:
            self.prior[c] = float(self.Nc[c]) / float(self.N)

            for w in self.V:
                self.prob[w] = {}
                Ncw = self.count_documents_from_class_term (c, w)
                self.prob[w][c] = (Ncw + 1.0) / (self.Nc[c] + 2.0)
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
            for w in self.V:
                if w in W:
                    score[c] += math.log(self.prob[w][c])
                else:
                    score[c] += math.log(1 - self.prob[w][c])

        return score
    # end def run

# end class Multivariate
