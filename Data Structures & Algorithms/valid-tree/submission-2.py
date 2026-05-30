from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs through the graph. Check if there are any CYCLES. 
        # a cycle means that we are not in a tree
        # being adjacent to your parent is fine - we can skip that
        
        indegrees = defaultdict(list)
        for a, b in edges:
            indegrees[a].append(b)
            indegrees[b].append(a)

        visited = set()

        def has_cycle(node: int, parent: int) -> bool:


            visited.add(node)
            for neighbor in indegrees[node]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                # genuine cycle in the graph
                    return True
                
                if has_cycle(neighbor, node):
                    return True
            
            return False

        if has_cycle(0, float('-inf')):
            return False  # gotta start from somewhere

        return len(visited) == n