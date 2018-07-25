# -*- coding: utf-8 -*-
from pathlib import Path

import urllib
import time
import requests

from bs4 import BeautifulSoup

print("Bitte einen 2ch-Link eingeben: ")
link = input()

r = requests.get(link)
# r = requests.get("https://2ch.hk/de/res/58444.html")
doc = BeautifulSoup(r.text, "html.parser")

message = []
imgUrl = []

for post in doc.select(".file-attr"):
    message.append(post.a["href"])
    imgUrl.append("https://2ch.hk" + post.a["href"])

print(imgUrl)
p = Path()
print(p.resolve())
# Unterordner images erstellen
Path(str(p.resolve()) + "\images").mkdir(parents=False, exist_ok=True)
# Aktuellen Zeitstempel holen und als Namen für einen weiteren Unterordner verwenden
datestamp = time.strftime("%d.%m.%Y %H-%M-%S")
Path(str(p.resolve()) + "\images" + "\\" + datestamp).mkdir(parents=False, exist_ok=True)

with open("images/thread.txt", encoding="utf-8", mode="a+") as file:
    file.write("----------------------------------------------------------" + "\n")
    file.write(time.strftime("%Y.%m.%d %H-%M-%S") + "\n")
    file.write("----------------------------------------------------------" + "\n")
    for element in imgUrl:
        file.write(element + "\n")

        urllib.request.urlretrieve(element, "images/" + datestamp + "/" + str(element.split("/")[-1]))
        time.sleep(0.5)
    file.write("\n")