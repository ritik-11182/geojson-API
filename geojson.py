import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True :
    add = input("enter the location : ")
    if len(add) < 1:
        break
    url = serviceurl + urllib.parse.urlencode({' address': add })
    print('retieving :', url)
    handle = urllib.request.urlopen(url).read()
    print('retrieved :', len(handle),'characters')
    js = json.loads(handle)
    print('place id', js['results'][0]['place_id'])
