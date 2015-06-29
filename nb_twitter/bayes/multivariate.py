# -*- coding: utf-8 -*-

# multivariate.py
# nb_twitter/nb_twitter/bayes
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-23
# Modified.........................2015-06-29
#
# This script was developed for use as part of the nb_twitter package


import math
from bayes import Bayes
from decorators import string_check


class Multivariate (Bayes):
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

    Multivariate Reference Page:
    http://nlp.stanford.edu/IR-book/html/htmledition/the-bernoulli-model-1.html

    """

    def train(self):
        """This method will train a multivariate naive bayes text classifier.
        The classifier will by trained using the provided classes and documents
        from the initializer.

        """

        for c in self.C:
            self.prior[c] = float(self.Nc[c]) / float(self.N)
            self.prob[c] = {}

            for w in self.V:
                Ncw = self.count_documents_from_class_term(c, w)
                self.prob[c][w] = (Ncw + 1.0) / (self.Nc[c] + 2.0)
    # end def train

    @string_check
    def run(self, d):
        """This method will run the trained multivariate naive bayes text
        classifier. This method will classify the provided document into
        a class.

        :param d: The new document to be classified.

        :return score: A dictionary of scores for this document in each class.

        """

        score = {}

        W = self.extract_words_from_document('multivariate', d)

        for c in self.C:
            score[c] = math.log(self.prior[c])
            for w in self.V:
                if w in W:
                    score[c] += math.log(self.prob[c][w])
                else:
                    score[c] += math.log(1 - self.prob[c][w])

        return score
    # end def run

    @string_check
    def count_documents_from_class_term(self, c, w):
        """This method will count the number of documents belonging to a class
        'c' that contain the word 'w'.

        :param c: The class of documents to count.

        :param w: The word a counted document must contain.

        :return Ncw: The count of documents in a class with a specific word.

        """

        Ncw = 0

        for d in self.D:
            if d[0] == c and w in d[1].split():
                Ncw += 1

        return Ncw
    # end def count_documents_from_class_term

# end class Multivariate
