class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]
                
                
                take = prod
                if i > 0 and j > 0:
                    take = prod + max(0, dp[i-1][j-1])
                
                
                skip1 = dp[i-1][j] if i > 0 else float('-inf')
                
           
                skip2 = dp[i][j-1] if j > 0 else float('-inf')
                
                dp[i][j] = max(take, skip1, skip2)
        
        return dp[n-1][m-1]
