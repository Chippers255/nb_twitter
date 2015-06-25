# -*- coding: utf-8 -*-

# stream.py
# nb_twitter/twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-25
#
# This script was developed for use as part of the nb_twitter package
# and utilizes Twitter's public streaming API, and the tweepy python
# interface

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "775039380-aHCGbAsE9iLIlnkBFB2aGf3Pj5t6kCVzUqq8WZfB"
access_token_secret = "Le3lXvk5v8yk0dPO2fvNNxhfpym5YMJEalamrkwIJRdMz"
consumer_key = "MJ7AQBA7kHz6KRoKLU572XYg1"
consumer_secret = "m4QeCGxgoiexo4S8zVh6OZBi0sEIZThKrQza2UBPuGBvMXDNFw"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])