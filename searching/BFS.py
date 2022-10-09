"""
BFS search
"""
import unittest

def BFS(graph: dict, node: str) -> list:
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

def BFS_SP(graph, start_node, target_node) -> list:
    # Set of visited nodes to prevent loops
    visited = []
    queue = []

    # Add the start_node to the queue and visited list
    visited.append(start_node)
    queue.append(start_node)
    
    # start_node has not parents
    parent = dict()
    parent[start_node] = None

    # Perform step 3
    path_found = False
    while queue:
        current_node = queue.pop(0) 
        if current_node == target_node:
            path_found = True
            break

        for next_node in graph[current_node]:
            if next_node not in visited:
                queue.append(next_node)
                parent[next_node] = current_node
                visited.append(next_node)
                
    # Path reconstruction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node]) 
            target_node = parent[target_node]
        path.reverse()
    return path 

class TestBFSSearch(unittest.TestCase):
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
        self.assertEqual(BFS(self.graph, '5'), ['5', '3', '7', '2', '4', '8'])

    def test_handles_unvisited_node(self):
        self.assertEqual(BFS(self.graph, '2'), ['2'])

    def test_handles_BFS_SP(self):
        self.assertEqual(BFS_SP(self.graph, '5', '2'), ['5', '3', '2'])
        self.assertEqual(BFS_SP(self.graph, '3', '8'), ['3', '4', '8'])
        self.assertEqual(BFS_SP(self.graph, '7', '8'), ['7', '8'])
        self.assertEqual(BFS_SP(self.graph, '7', '4'), [])
        self.assertEqual(BFS_SP(self.graph, '2', '4'), [])

if __name__ == "__main__":
    unittest.main()
