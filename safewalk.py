from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
   
        m = len(grid)
        n = len(grid[0])

        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

     
        if m == 1 and n == 1:
            return True

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

l
        best = [[-1] * n for _ in range(m)]
        best[0][0] = start_health

        q = deque([(0, 0, start_health)])

        while q:
            x, y, curr_health = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    new_health = curr_health - grid[nx][ny]

                    if new_health <= 0:
                        continue

                    if nx == m - 1 and ny == n - 1:
                        return True

                    if new_health > best[nx][ny]:
                        best[nx][ny] = new_health
                        q.append((nx, ny, new_health))

        return False
