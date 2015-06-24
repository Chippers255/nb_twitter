# -*- coding: utf-8 -*-

# bayes.py
# nb_twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <>
# Created..........................2015-06-24
# Modified.........................2015-06-24
#
# This script was developed for use as part of the nb_twitter package


class Bayes (object):
    """This abstract base class is the template for each of the different types
    of naive bayes text classifiers.

    """

    def __init__ (self, classes, documents):
        """The initializer method will define all required class variables
        calling all required methods to fill values.

        :param classes: A list of classes used to classify each document.

        :param documents: A list of documents to be used for training.

        :raise AssertionError: An error indicating classes or documents was not
                               of type list.

        """

        # Assert the class arguments are filled in properly
        assert type(classes) == list, "classes not a list: %r" % classes
        assert type(documents) == list, "documents not a list: %r" % documents

        self.C = classes  # A list of classes
        self.D = documents  # A list of document/class pairs
        self.N = len(documents)  # The number of training documents

        self.V  = []  # A list of all words in the training documents
        self.Nc = {}  # The number of training documents in each class

        self.prior = {}  # The probability of each class
        self.prob  = {}  # The conditional probability of each word to a class

        self.extract_vocabulary()
        self.count_class_documents()
    # end def __init__

    def extract_vocabulary (self):
        """This method will loop through each document and extract all original
        words and add them to the vocabulary list.

        :raise AssertionError: An error indicating document was not of type
                               list.

        """

        for d in self.D:
            assert type(d) == list, "document not a list: %r" % d
            for w in d[1].split():
                if w not in self.V:
                    self.V.append(w)
    # end def extract_vocabulary

    def count_class_documents (self):
        """This method will count the number of training documents belonging to
        each class.

        :raise AssertionError: An error indicating document was not of type
                               list.

        """

        for c in self.C:
            self.Nc[c] = 0
            for d in self.D:
                assert type(d) == list, "document not a list: %r" % d
                if c == d[0]:
                    self.Nc[c] += 1
    # end def count_class_documents

    def concatenate_class_documents (self, c):
        """This method will concatenate all the words of each document
        belonging to the provided class. This method will append every
        occurrence of a word.

        :param c: The class of training documents to concatenate.

        :raise AssertionError: An error indicating document was not of type
                               list.

        :return text: A concatenated list of all words belonging to a class.

        """

        text = []

        for d in self.D:
            assert type(d) == list, "document not a list: %r" % d
            if d[0] == c:
                text.extend(d[1].split())

        return text
    # end def concatenate_class_documents

    def extract_words_from_document (self, d):
        """This method will generate a list of all words in a provided
        document that are also present in our training word list.

        :param d: A non training document of text.

        :return W: A list of all vocabulary in the provided document.

        """

        W = []

        for w in d.split():
            if w in self.V:
                W.append(w)

        return W
    # end def extract_words_from_document

# end class Multinomial
