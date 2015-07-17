# -*- coding: utf-8 -*-

# test_listener.py
# nb_twitter/nb_twitter/test
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-07-17
# Modified.........................2015-07-17
#
# This script was developed for use as part of the nb_twitter package


"""This script was developed for use as part of the nb_twitter package and
utilizes Twitter's public streaming API, and the tweepy python interface.

"""


from nb_twitter.twitter import listener
from tweepy import OAuthHandler
from tweepy import Stream


# Variables that contains the user credentials to access Twitter API
access_token        = "775039380-aHCGbAsE9iLIlnkBFB2aGf3Pj5t6kCVzUqq8WZfB"
access_token_secret = "Le3lXvk5v8yk0dPO2fvNNxhfpym5YMJEalamrkwIJRdMz"
consumer_key        = "MJ7AQBA7kHz6KRoKLU572XYg1"
consumer_secret     = "m4QeCGxgoiexo4S8zVh6OZBi0sEIZThKrQza2UBPuGBvMXDNFw"


if __name__ == '__main__':
    l    = listener.Listener()
    auth = OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    stream.filter(track=['twitter'])