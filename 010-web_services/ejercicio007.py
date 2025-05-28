import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json

# https://apps.twitter.com/
# Create App and get the four strings, put then in hidden.py

TWITTER_URL = "http://api.twitter.com/1.1/friends/list.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print("")
    acct = input("Enter Twitter Account: ")
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": "5"})
    print("Retrieving", url)
    connection = urllir.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-limit-remaining"])
    js = json.loads(data)
    print(json.loads(js, indent=4))

    for u in js["users"]:
        print(u["screen_name"])
        s = u["status"]["text"]
        print("   ", s[:50])