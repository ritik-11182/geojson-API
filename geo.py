import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json
while true:
    url = 'http://py4e-data.dr-chuck.net/comments_418218.json'
    if len(url) < 1 :
        break
    print('retreiving', url)
    handle = urllib.request.urlopen(url).read()
    print('retieved', len(handle),'characters')
    try:
        js = json.loads(handle)
    except:
        js = None
    print(json.dump(js, indent = 3))
    sum = 0
    for s in js:
        sum = sum + int(s['comments']['count'])

print('total', sum)
