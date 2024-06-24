from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, parent, child):
        self.graph[parent].append(child)
        if not self.directed:
            self.graph[child].append(parent)

    def displayGraph(self):
        for key, value in self.graph.items():
            print(f"{key} 🔗 {', '.join(map(str,value))}")

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                parent, child = line.strip().split()
                self.addEdge(parent, child)
