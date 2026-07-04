from collections import defaultdict

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        stack = [1]
        ans = float('inf')

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for nei, dist in graph[node]:
                ans = min(ans, dist)
                if nei not in visited:
                    stack.append(nei)

        return ans