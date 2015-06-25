# -*- coding: utf-8 -*-

# multivariate.py
# nb_twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <>
# Created..........................2015-06-23
# Modified.........................2015-06-25
#
# This script was developed for use as part of the nb_twitter package


import math
import bayes


class Multivariate (bayes.Bayes):
    """The Bernoulli variation, as described by Manning et al (2008), generates
    a Boolean indicator about each term of the vocabulary equal to 1 if the
    term belongs to the examining document and 0 if it does not. The model of
    this variation is significantly different from Multinomial not only because
    it does not take into consideration the number of occurrences of each word,
    but also because it takes into account the non-occurring terms within the
    document. While in Multinomial model the non-occurring terms are completely
    ignored, in Bernoulli model they are factored when computing the
    conditional probabilities and thus the absence of terms is taken into
    account.

    Bernoulli model is known to make many mistakes while classifying long
    documents, primarily because it does not take into account the multiple
    occurrences of the words. Note that it is particularly
    sensitive to the presence of noisy features.

    """

    def train(self):
        """This method will train a multivariate naive bayes text classifier.
        The classifier will by trained using the provided classes and documents
        from the initializer.

        """

        for c in self.C:
            self.prior[c] = float(self.Nc[c]) / float(self.N)

            for w in self.V:
                self.prob[w] = {}
                Ncw = self.count_documents_from_class_term(c, w)
                self.prob[w][c] = (Ncw + 1.0) / (self.Nc[c] + 2.0)
    # end def train

    def run(self, d):
        """This method will run the trained multivariate naive bayes text
        classifier. This method will classify the provided document into
        a class.

        :param d: The new document to be classified.

        :return score: A dictionary of scores for this document in each class.

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
