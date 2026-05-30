from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # graph theory: in a tree nodes are N and edges must be N-1
        # quick check for that
        # make indegrees map
        # make visited set
        # do dfs and check if i visit all n nodes
        if len(edges) != n-1:
            return False
        
        indegrees = defaultdict(list)
        for a, b in edges:
            indegrees[a].append(b)
            indegrees[b].append(a)

        visited = set()

        def dfs(node: int):
            # base case
            if node in visited:
                return

            visited.add(node)
            for neighbor in indegrees[node]:
                dfs(neighbor)

        dfs(0) # gotta start from somewhere

        return len(visited) == n