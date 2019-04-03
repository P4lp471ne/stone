from bs4 import BeautifulSoup
from urllib.request import urlopen
from os import system
from typing import Dict
from pickle import dump

if __name__ == "__main__":
    html = urlopen("http://www.vstup.info/")
    bs = BeautifulSoup(html)
    tableId = "2018abet"
    blocklist = [i.find("a") for i in bs.find("table", {"id" : tableId}).find("tbody").findAll("tr")]
    dict = {}
    print(len(blocklist))
    for block in blocklist:
        dict[str(block.text)] = "http://www.vstup.info" + str(block['href'])
    print(dict)
    f = open("/home/palpatine/result","wb")
    dump(dict, f)
    f.close()
