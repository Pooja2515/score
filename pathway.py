from collections import deque
import math

class Solution(object):
    def findMaxPathScore(self, edges, online, k):


        n = len(online)

    
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = set()

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            costs.add(c)

      
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        temp_indegree = indegree[:]

        while q:
            node = q.popleft()
            topo.append(node)
            for nxt, _ in graph[node]:
                temp_indegree[nxt] -= 1
                if temp_indegree[nxt] == 0:
                    q.append(nxt)

        costs = sorted(costs)
        if not costs:
            return -1

        def can(score):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, c in graph[u]:
                    if c < score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    new_cost = dist[u] + c
                    if new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            score = costs[mid]

            if can(score):
                ans = score
                left = mid + 1
            else:
                right = mid - 1

        return ans
