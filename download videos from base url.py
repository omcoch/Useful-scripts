import urllib.request
import requests
from bs4 import BeautifulSoup

urls = ["http://location1.com", "http://example2.dev"]

i = 0  # global index, in use at downloadImg function for changing the name of each saved file


# download the images file from url and save in img directory (which must exists already!)
def downloadVideo(url, name):
    urllib.request.urlretrieve(url, "C:/Users/nocks/Documents/מדעי המחשב/reversing2021/" + name + ".mp4")


# run over thr urls array and apply the download for each url that contains the image
def doForAllUrls():
    for i in range(1, 14):
        downloadVideo("https://data.cyber.org.il/reversing/lev-tal/lesson"+str(i)+".mp4", str(i))
        print(str(i) + " complete successfully")
        downloadVideo("https://data.cyber.org.il/reversing/lev-tal/lesson"+str(i)+"a.mp4", str(i)+"a")
        print(str(i) + "a complete successfully")

doForAllUrls()
