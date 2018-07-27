# -*- coding: utf-8 -*-
from pathlib import Path
import urllib
from urllib.error import URLError, HTTPError, ContentTooShortError
import time
import requests
from bs4 import BeautifulSoup

import sys
if int(sys.version[0]) < 3:
    from proxy2 import *
else:
    from proxy3 import *

set_logging(True)
init()

checkFirstRun = True
url = ""


sendMessage("core:add-command", {"tag": "crawler:2ch", "info": "плагин для скачивания медиа-файлов с двачей"})

def crawler_2ch(sender, data):
    log_warn("inside function crawler_2ch now")
    global checkFirstRun
    global url

    if checkFirstRun:
        checkFirstRun = False
        sendMessage("DeskChan:say", {"text": "{user}, дай ссылку треда и я тебе всё-всё скачаю в /plugins/crawler2ch/",
                                     "skippable": False})
    else:
        if data["value"][0:14] == "https://2ch.hk" and len(data["value"]) > 28:
            url = data["value"]
        else:
            sendMessage("DeskChan:say", {"text": "Что-то непохоже это на ссылку..."})
            log_warn("URL Error exception, Invalid URL")
            return

        try:
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
        except URLError:
            sendMessage("DeskChan:say", {"text": "Что-то непохоже это на ссылку..."})
            log_warn("URL Error exception, Invalid URL")
            return


        message = []
        imgUrl = []

        for post in doc.select(".file-attr"):
            message.append(post.a["href"])
            imgUrl.append("https://2ch.hk" + post.a["href"])

        p = Path()
        # Create subfolder "images"
        Path(str(p.resolve()) + "/images").mkdir(parents=False, exist_ok=True)

        # Get actual timestamp which will be the name of the subfolder
        datestamp = time.strftime("%Y.%m.%d %H-%M-%S")
        Path(str(p.resolve()) + "/images" + "//" + datestamp).mkdir(parents=False, exist_ok=True)

        with open("images/thread.txt", encoding="utf-8", mode="a+") as file:
            sendMessage("gui:set-image", "happy")
            sendMessage("DeskChan:say", {"text": "Поиск файлов... Всё, начала скачивать."})
            file.write("----------------------------------------------------------" + "\n")
            file.write(time.strftime("%Y.%m.%d %H-%M-%S") + "\n")
            file.write("----------------------------------------------------------" + "\n")
            for element in imgUrl:
                file.write(element + "\n")
                try:
                    urllib.request.urlretrieve(element, "images/" + datestamp + "/" + str(element.split("/")[-1]))
                    # delay against a possible ip ban
                    time.sleep(0.3)
                except ContentTooShortError:
                    log("Download interrupted")
                    sendMessage("gui:set-image", "confusion")
                    sendMessage("DeskChan:say",
                                {"text": "{user}, тут ошибочка вышла, не всё скачалось. Попробуй ещё раз."})
            file.write("\n")
            sendMessage("gui:set-image", "happy")
            sendMessage("DeskChan:say", {"text": "Всё скачала, я хорошая, да?"})
            checkFirstRun = True
            return

    sendMessage("DeskChan:request-user-speech", None, crawler_2ch)


addMessageListener("crawler:2ch", crawler_2ch)

#Linking of command and event
sendMessage("core:set-event-link", {"eventName": "speech:get", "commandName": "crawler:2ch", "rule": "двач скачать"})

# plugin informations
setConfigField("dependencies", "python3")
setConfigField("author", "DeskChan Project <support@deskchan.info> (http://deskchan.info)")
setConfigField("short-description", {
                   "ru": "ДескЧан плагин: Краулер Двача",
                   "en": "DeskChan plagin: crawler 2ch"
               })
setConfigField("description", {
                   "ru": "Плагин запрашивает ссылку на тред Двача и скачивает все медиа-файлы и создаёт лог скачанного",
                   "en": "Plugin supports the user to download media files from the imageboard 2ch"
               })
setConfigField("name", {
                   "ru": "Краулер 2ch",
                   "en": "Crawler 2ch"
               })
setConfigField("link", "https://forum.deskchan.info/topic/129/python-crawler2ch-krauler-dvacha")
setConfigField("version", "1.0")



end_init()