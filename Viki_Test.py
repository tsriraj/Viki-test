from urllib.request import Request, urlopen
import json

def Get(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    data = json.loads(response)
    return data
    
url = 'http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page='

hdTrueTotal = 0
hdFalseTotal = 0
pageNum = 0
more = True

while(more == True):
    hd_true = 0
    hd_false = 0
    pageNum += 1

    jsonObj = Get(url + str(pageNum))
    response = jsonObj['response']

    for entry in response:
        hd = entry['flags']['hd']
        if (hd == True):
            hd_true += 1
        else:
            hd_false += 1

    hdTrueTotal += hd_true
    hdFalseTotal += hd_false

    print('For page number ' + str(pageNum) + ' HD is true = ' + str(hd_true) + " HD is false = " + str(hd_false))

    if (jsonObj['more'] == False):
        more = False

print("Number of HD = True: " + str(hdTrueTotal))
print("Number of HD = False: " + str(hdFalseTotal))