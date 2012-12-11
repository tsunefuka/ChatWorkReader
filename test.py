#!/usr/bin/python

import urllib, urllib2, cookielib, re

# url for login
url = "https://kcw.kddi.ne.jp/login.php"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1C28 Safari/419.3')]
urllib2.install_opener(opener)

# mail and pass
mail     = 'mail'
password = 'password'
r = opener.open(url, "email=%s&password=%s" % (mail, password))

print "Content-type: text/html; \n\n"
print 'success'

url2 = "https://kcw.kddi.ne.jp/#!rid1927770"
#url2 = "https://kcw.kddi.ne.jp/#"
f = opener.open(url2)
#f = urllib.urlopen(url)
html = f.read()
print html

