import os
import random
import re
import requests
import time
import urllib3

import collections

website = "https://midwayisd.org"
my_list = []
checked = []

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

except AttributeError:
    pass

def find_url(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)
	return [x[0] for x in url]

final = requests.get(website, verify = True)
checked.append(website)

test = find_url(final.text)
for x in test:
    check = "midwayisd.org" in x

    if check == True:
        my_list.append(x)
    #print(x)

possible_url = collections.Counter(my_list)
print(my_list)
print("\n\nbob:\n", list(possible_url))
print("total url:", len(my_list), "possible url:", len(possible_url))
'''
for x in my_list:
    if x == checked[]
'''
