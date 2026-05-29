from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # graph theory: Trees must have exactly n-1 edges
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int):
            if node in visited:
                return
            
            visited.add(node)
            for adj in graph[node]:
                dfs(adj)
        
        dfs(0)

        return len(visited) == n