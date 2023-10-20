from bs4 import BeautifulSoup
import os

# specify the directory you want to start from
rootDir = "D:/repos/leetcode-solutions/archive/university/WEB_lab8"

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith(".html"):
            with open(os.path.join(dirName, fname), "r+") as f:
                soup = BeautifulSoup(f, "html.parser")

                # Remove all class attributes
                for tag in soup():
                    if "class" in tag.attrs:
                        del tag.attrs["class"]

                # Write the changes back to the file
                f.seek(0)
                f.write(str(soup))
                f.truncate()
