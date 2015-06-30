# Bayes
This package contains all the required modules for a Naive Bayes text classifier. There is a main Bayes class, three subclasses of various implementations and a set of decorators for input assertation. 

## Bayes Class
his abstract base class is the template for each of the different types of naive bayes text classifiers.

## Multinomial Class
This model of Naive Bayes, as described by Manning et al (2008), estimates the conditional probability of a particular word given a class as the relative frequency of word 'w' in documents belonging to class 'c'.

This variation takes into account the number of occurrences of word 'w' in training documents from class 'c', including multiple occurrences.

## Multivariate Class
Also known as the Bernoulli variation, as described by Manning et al (2008), generatesa Boolean indicator about each term of the vocabulary equal to 1 if the term belongs to the examining document and 0 if it does not. The model of this variation is significantly different from Multinomial not only because it does not take into consideration the number of occurrences of each word, but also because it takes into account the non-occurring terms within the document. While in Multinomial model the non-occurring terms are completely ignored, in Bernoulli model they are factored when computing the conditional probabilities and thus the absence of terms is taken into account.

Bernoulli model is known to make many mistakes while classifying long documents, primarily because it does not take into account the multiple occurrences of the words. Note that it is particularly sensitive to the presence of noisy features.

## Binarized Class
This model of Naive Bayes, as described by Dan Jurafsky, is identical to the Multinomial Naive Bayes model with only difference that instead of measuring all the occurrences of the term t in the document, it measures it only once. The reasoning behind this is that the occurrence of the word matters more than the word frequency and thus weighting it multiple times does not improve the accuracy of the model.

Both the training and the running algorithms remain the same with only exception that instead of using multiple occurrences we clip all word counts in each document at 1.
