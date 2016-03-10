#! /bin/env python 


'''
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
'''

import os
import re

os.chdir('/tmp/tmpMcLQzy/')
print os.getcwd()



def next_opn(fnum):
    #fnum
    f=open(fnum,'r')
    l=re.findall('(\d+)',f.read())
    #w=re.findall(r'.*',f.read())
    #print w
    print l[0]
    f.close()
    #while True:
    try:
          next_opn(str(l[0])+'.txt')
    except:
          
          return l[0] 

next_opn('90052.txt')

