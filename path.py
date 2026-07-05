class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(board)

        # dpScore[i][j] = maximum score from (i,j) to S
        # dpWays[i][j] = number of maximum-score paths
        dpScore = [[-1] * n for _ in range(n)]
        dpWays = [[0] * n for _ in range(n)]

        # Starting point S
        dpScore[n - 1][n - 1] = 0
        dpWays[n - 1][n - 1] = 1

        # Process from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                maxScore = -1
                ways = 0

                # Down
                if i + 1 < n and dpScore[i + 1][j] != -1:
                    if dpScore[i + 1][j] > maxScore:
                        maxScore = dpScore[i + 1][j]
                        ways = dpWays[i + 1][j]
                    elif dpScore[i + 1][j] == maxScore:
                        ways = (ways + dpWays[i + 1][j]) % MOD

                # Right
                if j + 1 < n and dpScore[i][j + 1] != -1:
                    if dpScore[i][j + 1] > maxScore:
                        maxScore = dpScore[i][j + 1]
                        ways = dpWays[i][j + 1]
                    elif dpScore[i][j + 1] == maxScore:
                        ways = (ways + dpWays[i][j + 1]) % MOD

                # Diagonal
                if i + 1 < n and j + 1 < n and dpScore[i + 1][j + 1] != -1:
                    if dpScore[i + 1][j + 1] > maxScore:
                        maxScore = dpScore[i + 1][j + 1]
                        ways = dpWays[i + 1][j + 1]
                    elif dpScore[i + 1][j + 1] == maxScore:
                        ways = (ways + dpWays[i + 1][j + 1]) % MOD

                if maxScore == -1:
                    continue

                value = 0
                if board[i][j] not in ('E', 'S'):
                    value = int(board[i][j])

                dpScore[i][j] = maxScore + value
                dpWays[i][j] = ways % MOD

        if dpWays[0][0] == 0:
            return [0, 0]

        return [dpScore[0][0], dpWays[0][0]]