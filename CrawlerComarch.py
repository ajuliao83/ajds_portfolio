import requests
import json
import time
import csv

bearer_token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFubmVsIjoiViIsImNsaWVudF9pZCI6IlllSlJqOTZ1YXhVamNMd0hGOXpEc1E9PSIsImNsbV91c2VyX2lkIjoiV3U2ZklYVHRjQUpWZHptM1pNVU5oZz09IiwiZXhwIjoxNjY5Mzk1Njc5LCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwianRpIjoiMDk5NmIxYzQtYTMxOS00NWU2LTg3ZDQtOWM5MjEwZWQzZjNkIiwic2NvcGUiOlsiYW55Il0sInZlcnNpb24iOiIxNjY5MzA5MDM5MTgyIn0.AkT6UBof0ItndjDQ--elgsYKaxsKC1BpirFO0W_8qis'
url_base = ''

def loopIds():
    

    with open('data.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
    for row in datareader:
                print(row(0))



def getIdentifierInformation():
    request_url=url_base + 'b2b/profile/identifiers/' + IdentifierId
    response= requests.get(request_url,timeout=60,headers=headers)
    response_text=response.json()

    loopIds()

