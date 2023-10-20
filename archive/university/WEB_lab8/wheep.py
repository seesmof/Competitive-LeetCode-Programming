import os
from bs4 import BeautifulSoup

rootDir = "D:/repos/leetcode-solutions/archive/university/WEB_lab8"

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith(".html"):
            filePath = os.path.join(dirName, fname)
            with open(filePath, "r+", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                for tag in soup():
                    if tag.has_attr("class"):
                        del tag["class"]
                f.seek(0)
                f.write(str(soup.prettify()))
                f.truncate()
