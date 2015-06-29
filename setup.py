# -*- coding: utf-8 -*-

# setup.py
# nb_twitter
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#            Preston Engstrom <pe12nh@brocku.ca>
# Created..........................2015-06-26
# Modified.........................2015-06-26
#
# This script was developed for use as part of the nb_twitter package


from setuptools import setup, find_packages


def read(data, file_name):
    """This function is to be used by the setup.py file to read required setup
    metadata from files.

    :file_name: A string containing the path/file name of a file containing
                required setup metadata.

    :raise IOError: Raises if the desired file is missing.

    :return content: The metadata read from the provided file.

    """

    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except IOError:
        print('You are missing a ' + data + ' file!')
        raise

    return content
# end def read


# Create the metadata for the setup file
_name = 'NB_Twitter'
_version = read('version', 'version')
_license = read('license', 'LICENSE')
_author = 'Thomas Nelson, Preston Engstrom'
_author_email = 'tn90ca@gmail.com, pe12nh@brocku.ca'
_url = 'https://github.com/Chippers255/nb_twitter'
_download_url = 'https://github.com/Chippers255/nb_twitter/releases'
_description = 'A Naive Bayes implementation to classify the mood of tweets.'

# Define the packages to install from this module
_packages = find_packages(exclude=('test*', ))

# Define required packages to be installed with nb_twitter
_requires = ['tweepy', 'ujson']

# Define keywords associated with this module
_keywords = 'twitter naive bayes mood moods classifier classify text tweepy ' \
            'nb_twitter'


setup(
    name=_name,
    version=_version,
    license=_license,
    author=_author,
    author_email=_author_email,
    url=_url,
    download_url=_download_url,
    description=_description,
    packages=_packages,
    include_package_data=True,
    install_requires=_requires,
    keywords=_keywords,
    classifiers=['Development Status :: 1 - Planning',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4'],
    )
