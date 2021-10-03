import urllib.request
import requests
from bs4 import BeautifulSoup


urls = ["http://location1.com", "http://example2.dev"]

i = 0  # global index, in use at downloadImg function for changing the name of each saved file


# download the images file from url and save in img directory (which must exists already!)
def downloadImg(imgUrl):
    global i
    urllib.request.urlretrieve(imgUrl, "img/"+str(i)+".jpg")
    i += 1


# search into the html for thr <img> element and get out the specific src url of the images
def fetchOnlyImgUrl(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    link = soup.find('img')
    return link['src']


# run over thr urls array and apply the download for each url that contains the image
def doForAllUrl():
    for url in urls:
        downloadImg(fetchOnlyImgUrl(url))
        

doForAllUrl()
