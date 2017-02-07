from urllib.parse import urlencode
import urllib.request
import json
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
#import cookielib
import http.cookiejar

uname = "----"
passwd = "----"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

# Request key
url = 'https://steamcommunity.com/login/getrsakey/'
values = {'username' : uname, 'donotcache' : str(int(time.time()*1000))}
headers = { 'User-Agent' : user_agent }
post = urlencode(values)
req = urllib.request.Request(url, post, headers)
response = urllib.request.urlopen(req).read()
data = json.loads(response)

print ("Get Key Success:", data["success"])

# Encode key
mod = long(str(data["publickey_mod"]), 16)
exp = long(str(data["publickey_exp"]), 16)
rsa = RSA.construct((mod, exp))
cipher = PKCS1_v1_5.new(rsa)
print (base64.b64encode(cipher.encrypt(passwd)))

# Login
url2 = 'https://steamcommunity.com/login/dologin/'
values2 = {
        'username' : uname,
        "password": base64.b64encode(cipher.encrypt(passwd)),
        "emailauth": "",
        "loginfriendlyname": "",
        "captchagid": "-1",
        "captcha_text": "",
        "emailsteamid": "",
        "rsatimestamp": data["timestamp"],
        "remember_login": False,
        "donotcache": str(int(time.time()*1000)),
}
headers2 = { 'User-Agent' : user_agent }
post2 = urllib.urlencode(values2)
req2 = urllib.request(url2, post2, headers)
response2 = urllib.request.urlopen(req2).read()
data2 = json.loads(response2)

if data2["success"]:
        print ("Logged in!")
else:
        print ("Error, could not login:", data2["message"])

print (response2)
