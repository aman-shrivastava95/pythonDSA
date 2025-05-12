import math

class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsCombinatorial(self, m, n):
      total = m - 1 + n - 1
      return math.comb(total, m-1)
