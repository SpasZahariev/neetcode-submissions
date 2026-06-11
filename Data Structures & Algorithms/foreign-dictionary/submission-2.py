from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # if given words are not lexicographically sorted => ""

        # todo input validation

        # return 1 string. Can be any of the possible solutions
        # 1. create adj sets and count the number of in_degree for each node
        # some chars depend on other ones going before them a -> b (a before b)
        # 2. count the number of vertices
        # 3. topologically sort and store results. Start with vertices that don't have any dependencies (in_degree == 0)

        unique_chars = {c for w in words for c in w}
        adj = {c:set() for c in unique_chars}
        in_degree = {c:0 for c in unique_chars}

        # check lexicographic sorting
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            # check for impossible sort
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # find dependencies
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    # we found the dependency
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break
        
        # topological sort time
        queue = deque([c for c in adj if in_degree[c] == 0])
        res = []
        while queue:
            free_char = queue.popleft()
            res.append(free_char)

            for nei in adj[free_char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        # check if there are nodes we have not covered (there is a cyclic dependency)
        if len(res) != len(unique_chars):
            return ""
        return "".join(res)
