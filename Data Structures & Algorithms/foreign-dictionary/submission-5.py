from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build an in degree dict for letters and a count of prerequisites that come before them
        # build a graph of chars and their neighbors
        # have a way of checking the count of unique characters
        # do topological sort

        # todo input validation
        if not words:
            return ""

        graph = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in graph}
        char_count = len(indegree)

        # populate graphs
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            # check if impossible lexographic sort
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            # now we can find the first mismatch
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        indegree[c2] += 1
                        graph[c1].add(c2)
                    break
        
        # now we can do a topological sort
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)

            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # check if we were able to go through all the dependencies (indegree connections)
        if len(res) != char_count:
            # there must be a cyclic dependency
            return ""
        return "".join(res)
