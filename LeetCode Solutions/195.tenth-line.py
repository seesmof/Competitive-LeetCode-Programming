from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
dataFolder = path.join(currentDir, "..", "data")
lineyFile = path.join(dataFolder, "195-lotta-lines.txt")

lines = []

with open(lineyFile, "r") as file:
    for line in file:
        lines.append(line.strip())

if len(lines) > 9:
    tenthLine = lines[9]
    console.print(tenthLine, style="italic")
else:
    console.print("[red]The file has less than 10 lines.[/red]")
