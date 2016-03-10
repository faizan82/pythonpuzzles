#! /bin/env python 

import urllib, zipfile
from zipfile import ZipFile
from tempfile import mktemp
#import urllib2

#req=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')

#print req.read()


urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip','channel.zip')
dest=mktemp()
fil=ZipFile('channel.zip')
fil.extractall(dest)
fil.close()

