from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # build the adjacency lists
        # build the in_degree counts
        # check for impossible lexicographical ordering (shared prefix but first word longer)
        # build res with topological sort on adjacency lists

        adj = {}
        in_degree = {}
        for w in words:
            for c in w:
                adj[c] = set()
                in_degree[c] = 0

        num_vertices = len(adj) # number of characters

        # build the edges (dependencies following) in the adj list
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]

            # check for invalid lexicographical ordering
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # populate our adj and in_degree
            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                # found a bigger char
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2]+=1
                    break
        
        # NOW we can do topological sort on the graphs (and potentially find a cycle)
        res = []
        queue = deque([key for key, val in in_degree.items() if val == 0])

        while queue:
            c = queue.popleft()
            res.append(c)
            # todo think about cycle detection
            for nei in adj[c]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        if num_vertices != len(res):
            # unresolvable dependencies => not a DAG
            return ""

        return "".join(res)