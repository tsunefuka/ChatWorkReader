#!/usr/bin/python

import urllib, urllib2, cookielib, re

url = "https://kcw.kddi.ne.jp/login.php"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

mail     = 'tsunefuka-k@klab.com'
password = 'Eucharis729'
r = opener.open(url, "email=%s&password=%s" % (mail, password))

print "Content-type: text/html; \n\n"
print 'success'

url2 = "https://kcw.kddi.ne.jp/#!rid1927770"
f = opener.open(url2)
#f = urllib.urlopen(url)
html = f.read()
print html

