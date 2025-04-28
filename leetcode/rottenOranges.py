from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        R = len(grid)
        C = len(grid[0])
        fresh = 0
        time = 0 

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        #start multisource bfs    
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                #process all four directions
                for dx, dy in directions:
                    r_new, c_new = r + dx, c + dy
                    if (r_new < 0 or 
                       c_new < 0 or 
                       r_new >= len(grid) or 
                       c_new >= len(grid[0]) 
                       or grid[r_new][c_new] != 1):
                        continue
                    #mark this orange as rotten and add it to the queue
                    grid[r_new][c_new] = 2
                    fresh -= 1
                    q.append((r_new, c_new))
            time+=1
        
        return time if fresh == 0 else -1

