# -*- coding: utf-8 -*-

# decorators.py
# nb_twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-25
# Modified.........................2015-06-25
#
# This script was developed for use as part of the nb_twitter package


import time


def constructor(func):
    """This decorator will check that all variables passed to the NB's
    initializer method are in the correct format.

    """

    def wrapper(*args):
        assert type(args[0]) == list, "classes not a list: %r" % args[0]
        assert type(args[1]) == list, "documents not a list: %r" % args[1]

        for c in args[0]:
            assert type(c) == str, \
                "classes contains a non string value: %r" % args[0]

        for d in args[1]:
            assert type(d) == list, \
                "documents contains a non list value: %r" % d
            assert type(d[0]) == str, \
                "documents contains a non string value: %r" % d
            assert type(d[1]) == str, \
                "documents contains a non string value: %r" % d

        return func(*args)
    # end def wrapper

    return wrapper
# end def t_decorator

def string_check(func):
    """This decorator will check that all variables passed to the function
    are in the correct format.

    """

    def wrapper(*args):

        for x in range(len(args)):
            if x > 0:
                assert type(args[x]) == str, \
                    "argument not a string: %r" % args[x]

        return func(*args)
    # end def wrapper

    return wrapper
# end def t_decorator

def time_function(func):
    """This decorator will output the time a function takes to execute.

    """

    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()

        print("Time it took to run " + func.__name__ + ": " + str(t2 - t1))
    # end def wrapper

    return wrapper
# end def time_function
