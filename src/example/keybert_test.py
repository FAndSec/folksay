# use miniconda to config dependency
import sys
import os
from os.path import dirname

pwd = os.path.abspath(__file__)
sys.path.insert(0,dirname(dirname(dirname(pwd))))
# print (sys.path)
import keybert._maxsum


print ('finish')