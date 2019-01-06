import json
import scrapy
import urllib.parse
from scrapy import Spider, Request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time
import pickle
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#soup = BeautifulSoup(html_doc, 'html.parser')
#atexts = soup.select('a')
#print(atexts[0].text())

str = u'陈奕迅演唱(十年)'
list = re.findall('\((.*?)\)', str)
print(''.join(list))
print(list[0])


