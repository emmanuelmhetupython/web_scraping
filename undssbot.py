import bs4
import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'http://zimbabwe.shafaqna.com/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
LatestHeadlines = page_soup.find_all("div",{"class":"news-box"})
csvfile = "eunice.csv"
f = open(csvfile,"w")
header = "Allheadlines,\n"
f.write(header)
header = LatestHeadlines[0]
for header in LatestHeadlines:
    Allheadlines = header.h2.text
    print("Headline :" + Allheadlines)
    f.write(Allheadlines)
f.close()
