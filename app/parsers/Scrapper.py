from bs4 import BeautifulSoup
from urllib.request import urlopen
from os import system

if __name__ == "__main__":
    f = open("/home/palpatine/result","w")
    html = urlopen("http://vstup.info/2018/i2018i41.html")
    wordToLookFor = input("textToFind:").lower()
    bs = BeautifulSoup(html)
    print(bs.prettify())
    f.write("<html>")
    f.write("<body>\n<meta charset=\"UTF-8\">\n")
    blocklist = bs.find("table", {"id": "denna1"}).find("tbody").findAll("tr")
    print(len(blocklist))
    for block in blocklist:
        if block.get_text().lower().find(wordToLookFor) != -1:
            f.write(str(block).replace("href=\".", "href=\"http://vstup.info/2018/") + "\n")
            f.write("<hr>")
    f.write("</body>")
    f.write("</html>")
    f.close()
    system("firefox ~/result")