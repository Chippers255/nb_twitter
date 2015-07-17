# -*- coding: utf-8 -*-

# listener.py
# nb_twitter/nb_twitter/twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-07-09
# Modified.........................2015-07-17
#
# This script was developed for use as part of the nb_twitter package


import time
from tweepy.streaming import StreamListener


class Listener (StreamListener):
    """This class...

    """

    def __init__(self, time_limit=10):
        """This method...

        """

        self.time = time.time()
        self.limit = time_limit
    # end def __init__

    def on_data(self, data):
        """This method...

        """

        if (time.time() - self.time) < self.limit:
            try:
                out_file = open('raw_tweets.json', 'a')
                out_file.write(data)
                out_file.write('\n')
                out_file.close()
            except BaseException as e:
                print("Method on_data failed to run: " + e)
        else:
            print("Listener exceeded time limit, shutting down now.")
            exit()

        return True
    # end def on_data

    def on_error(self, status):
        print(status)
    # end def on_error

# end class Listener
