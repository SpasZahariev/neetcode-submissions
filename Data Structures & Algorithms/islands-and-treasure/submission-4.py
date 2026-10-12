from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # todo input validation

        # I need to use breadth first traversal queue
        # update nodes increasingly when i find a 0
        # if I hit a boundary, a -1, or a value smaller than my cur_counter. Stop!
        # Simultanious BFS!!!!

        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def bfs():
            row, col, cur = queue.popleft()
            # boundary checks
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in visited or
                grid[row][col] < cur):
                return
            
            visited.add((row, col))
            grid[row][col] = cur

            for dr, dc in directions:
                queue.append((row+dr, col+dc, cur+1))

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    
        while queue:
            bfs()