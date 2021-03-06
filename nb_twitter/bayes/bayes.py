# -*- coding: utf-8 -*-

# bayes.py
# nb_twitter/nb_twitter/bayes
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-24
# Modified.........................2015-06-30
#
# This script was developed for use as part of the nb_twitter package


import nb_twitter.bayes.decorators as decorators


class Bayes (object):
    """This abstract base class is the template for each of the different types
    of naive bayes text classifiers.

    """

    @decorators.constructor
    def __init__(self, classes, documents):
        """The initializer method will define all required class variables
        calling all required methods to fill values.

        :param classes: A list of classes used to classify each document.

        :param documents: A list of documents to be used for training.

        """

        self.C = classes  # A list of classes
        self.D = documents  # A list of document/class pairs
        self.N = len(documents)  # The number of training documents

        self.V = []  # A list of all words in the training documents
        self.Nc = {}  # The number of training documents in each class

        self.prior = {}  # The probability of each class
        self.prob = {}  # The conditional probability of each word to a class

        self.extract_vocabulary()
        self.count_class_documents()
    # end def __init__

    def extract_vocabulary(self):
        """This method will loop through each document and extract all original
        words and add them to the vocabulary list.

        """

        for d in self.D:
            for w in d[1].split():
                if w not in self.V:
                    self.V.append(w)
    # end def extract_vocabulary

    def count_class_documents(self):
        """This method will count the number of training documents belonging to
        each class.

        """

        for c in self.C:
            self.Nc[c] = 0
            for d in self.D:
                if c == d[0]:
                    self.Nc[c] += 1
    # end def count_class_documents

    @decorators.string_check
    def extract_words_from_document(self, sub_class, d):
        """This method will generate a list of all words in a provided
        document that are also present in our training word list.

        :param sub_class: The type of subclass using this method

        :param d: A non training document of text.

        :return W: A list of all vocabulary in the provided document.

        """

        W = []

        for w in d.split():
            if w in self.V:
                if sub_class == 'binarized' and w in W:
                    pass
                else:
                    W.append(w)

        return W
    # end def extract_words_from_document

# end class Multinomial
