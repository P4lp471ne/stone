from bs4 import BeautifulSoup
from urllib.request import urlopen
from os import system
from typing import List

class Scrapper:
    def __init__(self, html):
        self.html = html
        self.tablesIds = [[i.a.getText().replace("\n", "").replace("    ", "")[:i[0].find("(")], str(i.a.get("href")).replace("#", "")] for i in bs.find("ul", {"id": "myTab"}).findAll("li")]

    def scrap(self, request):
        response = [{'name':i[0], 'extractedLinks': List[str]} for i in self.tablesIds]
        counter = 0
        for i in self.tablesIds:
            blocklist = bs.find("div", {"id": i[1]}).find("table").find("tbody").findAll("tr")
            for block in blocklist:
                if block.get_text().lower().find(wordToLookFor) != -1:
                    response[counter]['extractedLinks'].append(str(block).replace("href=\".", "href=\"http://vstup.info/2018/") + "\n")
            counter += 1
        return response


if __name__ == "__main__":
    f = open("/home/palpatine/result","w")
    html = urlopen("http://vstup.info/2018/i2018i41.html")
    wordToLookFor = input("textToFind:").lower()
    bs = BeautifulSoup(html)
    f.write("<html>")
    f.write("<body>\n<meta charset=\"UTF-8\">\n")
    tablesIds = [[i.a.getText().replace("\n", "").replace("    ", ""), str(i.a.get("href")).replace("#", "")] for i in bs.find("ul", {"id": "myTab"}).findAll("li")]
    for i in tablesIds:
        blocklist = bs.find("div", {"id": i[1]}).find("table").find("tbody").findAll("tr")
        f.write("<tr><td><h1>" + i[0][:i[0].find("(")] + "</h1></td></tr>")
        f.write("<hr>")
        print(len(blocklist))
        for block in blocklist:
            if block.get_text().lower().find(wordToLookFor) != -1:
                f.write(str(block).replace("href=\".", "href=\"http://vstup.info/2018/") + "\n")
                f.write("<hr>")
    f.write("</body>")
    f.write("</html>")
    f.close()
    system("firefox ~/result")
