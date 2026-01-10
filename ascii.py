class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        
        # dp[i][j] = minimum ASCII delete sum to make s1[i:] and s2[j:] equal
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: s2 exhausted, delete remaining s1 characters
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        
        # Base case: s1 exhausted, delete remaining s2 characters
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])
        
        # Fill DP table
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )
        
        return dp[0][0]
