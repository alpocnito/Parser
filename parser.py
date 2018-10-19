# from bs4 import BeautifulSoup
# import urllib.request as urllib2
#
# url = 'https://www.investing.com/equities/apple-computer-inc'
#
# headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
# req = urllib2.Request("https://www.investing.com/equities/apple-computer-inc-technical", headers=headers)
# soup = BeautifulSoup(urllib2.urlopen(req), 'html.parser')
#
# a = soup.find_all(class_="first left symbol")
# tech_analize = {}
# for b in a:
#     tech_analize[b.string] = b.parent.find('span').text.strip('\n\t\t\t\t\t')
# print(tech_analize)
import requests
url = "http://www.sentic.net/api/en/concept/meet/polarity/intensity"
r = str(requests.get(url).content)
if int(r.find('ERROR')) == -1:
    r = r[360:372]
    r = r[r.find(">") + 1:]