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

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 0:
                    queue.append((i, j))
                    
        # bfs
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        dist = 0
        while queue:
            dist+=1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    # boundary checks
                    if (row < 0 or row >= ROWS or
                        col < 0 or col >= COLS or
                        grid[row][col] <= dist):
                        continue
                    grid[row][col] = dist
                    queue.append((row, col))


            
