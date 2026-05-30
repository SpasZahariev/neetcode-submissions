from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build a graph, an array of sets connections, a set of visited nodes

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        connections = 0
        visited = set()

        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
                
        for i in range(n):
            if i in visited:
                continue
            
            dfs(i)
            connections += 1
        
        return connections

