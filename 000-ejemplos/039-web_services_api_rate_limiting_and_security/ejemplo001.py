import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = "http://api.twitter.com/1.1/friends/list.json"

while True:
    print("")
    acct = input("Enter Twitter Account: ")
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": "5"})
    print("Retrieving", url)
    connection = urllir.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-limit-remainig"])
    js = json.loads(data)
    print(json.loads(js, indent=4))

    for u in js["users"]:
        print(u["screen_name"])
        s = u["status"]["text"]
        print("   ", s[:50])
