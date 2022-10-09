"""
DFS search
"""
import unittest
from typing import Any

def dfs(graph:dict , node: Any, stack: list, visited: list = None):  #function for dfs 
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, stack, visited)
        stack.append(node)
    return visited

def topologicalSort(graph):
    visited = []
    stack = []

    for i in graph.keys():
        if i not in visited:
            dfs(graph, i, stack, visited)
    stack.reverse()
    return stack

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
        self.graph1 = {
            '6' : [],
            '0' : [],
            '1' : [],
            '2' : ['3'],
            '3' : ['1'],
            '4' : ['0', '1'],
            '5' : ['2','0']
        }


    def test_handles_visited_node(self):
        self.assertEqual(dfs(self.graph, '5', []), ['5', '3', '2', '4', '8', '7'])
        self.assertEqual(dfs(self.graph, '3', []), ['3', '2', '4', '8'])
        self.assertEqual(dfs(self.graph, '8', []), ['8'])

    def test_handles_topologicalSort(self):
        self.assertEqual(topologicalSort(self.graph), ['5', '7', '3', '4', '8', '2'])
        self.assertEqual(topologicalSort(self.graph1), ['5', '4', '2', '3', '1', '0','6'])

if __name__ == "__main__":
    unittest.main()