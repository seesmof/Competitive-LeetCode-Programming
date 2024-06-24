from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


import requests

url = "https://api.biblegateway.com/2/search/verses.php"
params = {
    "json": {
        "book": "Matthew",
        "bid": "40",
        "chapter": "19",
        "chapter_roman": "XIX",
        "verse": "26",
        "found": 1,
        "next_chapter": "read-mat-20",
        "version": "nasb",
    }
}

response = requests.get(url, params=params)
console.print(response)

"""
data = response.json()

parsed_data = f'"{data["text"]}"—{data["book"]} {data["chapter"]}:{data["verses"]} [{data["version"].upper()}]'
print(parsed_data)
"""
