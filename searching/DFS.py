"""
DFS search
"""
import unittest
from typing import Any

def DFS(graph:dict , node: Any, visited: list = None):  #function for dfs 
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            DFS(graph, neighbour, visited)
    return visited

class TestDFSSearch(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph = {
            '5' : ['3','7'],
            '3' : ['2', '4'],
            '7' : ['8'],
            '2' : [],
            '4' : ['8'],
            '8' : []
        }


    def test_handles_visited_node(self):
        self.assertEqual(DFS(self.graph, '5'), ['5', '3', '2', '4', '8', '7'])
        self.assertEqual(DFS(self.graph, '3'), ['3', '2', '4', '8'])
        self.assertEqual(DFS(self.graph, '8'), ['8'])

if __name__ == "__main__":
    unittest.main()