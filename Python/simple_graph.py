from collections import deque

class Graph():
    def __init__(self,connections,directed=False):
        self.graph = {}
        self.directed = directed
        self.add_connections(connections)

    def add_connections(self,connections):
        for node1,node2 in connections:
            self.add(node1,node2)

    def add(self,node1,node2):
        if node1 not in self.graph:
            self.graph[node1] = set()

        self.graph[node1].add(node2)

        if self.directed is False:
            if node2 not in self.graph:
                self.graph[node2] = set()

            self.graph[node2].add(node1)

    def remove(self,node):
        for n in self.graph:
            try:
                self.graph[n].remove(node)
            except KeyError:
                pass
        try:
            del self.graph[node]
        except KeyError:
            pass

    def is_connected(self,node1,node2):
        return node1 in self.graph and node2 in self.graph[node1]

    def find_path(self,node1,node2,path=[]):    # DFS Method 1, returns path
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self.graph:
            return None
        for node in self.graph[node1]:
            if node not in path:
                new_path = self.find_path(node,node2,path)
                if new_path:
                    return new_path
        return None

    def hasPathDFS(self,node1,node2,visited = set()): # DFS Method 2, returns bol
        if node1 in visited:
            return False
        visited.add(node1)
        if node1 == node2:
            return True
        for node in self.graph[node1]:
            if node not in visited:
                if self.hasPathDFS(node,node2,visited):
                    return True
        return False

    def hasPathBFS(self,node1,node2):
        visited = set()
        nextToVisit = deque()
        nextToVisit.append(node1)

        while nextToVisit:
            node = nextToVisit.pop()
            if node == node2:
                return True
            if node not in visited:
                visited.add(node)
                for dest in self.graph[node]:
                    nextToVisit.append(dest)
        return False





# Testing
connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
                ('C', 'D'), ('E', 'F'), ('F', 'C')]
# g = Graph(connections, directed=True)
g = Graph(connections, directed=False)

print(g.graph)
print(g.find_path('A','E'))
print(g.hasPathDFS('A','F'))
print(g.hasPathBFS('A','C'))