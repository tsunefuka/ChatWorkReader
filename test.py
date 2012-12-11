#!/usr/bin/python

import urllib

url = "https://kcw.kddi.ne.jp/#!rid1927770"
f = urllib.urlopen(url)
html = f.read()

print "Content-type: text/html; \n\n"
print html

