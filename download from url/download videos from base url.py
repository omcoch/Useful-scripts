import urllib.request
import requests
from bs4 import BeautifulSoup

ext = "mp4"


# download the images file from url and save in img directory (which must exists already!)
def downloadVideo(url, name):
    try:
        urllib.request.urlretrieve(url, "C:/Users/me/directory" + name + ".mp4")
        print(name + " complete successfully!")
    except Exception as e:
        print("file probably doesn't exists...")


# run over thr urls array and apply the download for each url that contains the image
def doForAllUrls():
    for i in range(2, 14):
        name = str(i)
        downloadVideo("https://data.example.com/lesson" + name + ".mp4", name)  # first url in this iteration
        name = str(i) + "a"
        downloadVideo("https://data.example.com/lesson" + name + ".mp4", name)  # another url uses the same iteration
    print("*************** We're done for today, thank you. ***************")


doForAllUrls()
