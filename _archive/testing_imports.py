import json
from time import sleep
import inquirer
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install
from typing import List
import matplotlib.pyplot as plt
import networkx as nx

install()
console = Console()


def readFile(name: str):
    with open(name, "r", encoding="utf-8") as file:
        return file.read()


def writeFile(name: str, content: str):
    with open(name, "w", encoding="utf-8") as file:
        file.write(content)


def readJson(name: str):
    with open(name, "r", encoding="utf-8") as file:
        return json.load(file)


def writeJson(name: str, content: dict):
    with open(name, "w", encoding="utf-8") as file:
        json.dump(content, file)


def readInputString(varName: str):
    questions = [
        inquirer.Text(variable=varName, message=f"Enter {varName}", name=varName)
    ]
    answers = inquirer.prompt(questions)
    return answers[varName]
