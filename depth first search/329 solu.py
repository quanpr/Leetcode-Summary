from copy import deepcopy
import sys
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(matrix, idx, prev, dp):
            x, y = idx
            m, n = len(matrix), len(matrix[0])
            if x < 0 or y < 0 or x >= m or y >= n:
                return 0
            else:
                cur = matrix[x][y]
                if cur <= prev:
                    return 0
                else:
                    if dp[x][y]:
                        return dp[x][y]
                    
                    Len = 1 + max(dfs(matrix, (x-1, y), cur, dp),
                                  dfs(matrix, (x+1, y), cur, dp),
                                  dfs(matrix, (x, y-1), cur, dp),
                                  dfs(matrix, (x, y+1), cur, dp))
                    dp[x][y] = Len
                    return Len
                
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        r, dp = 0, [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r = max(r, dfs(matrix, (i, j), -sys.maxsize, dp))
        return r
                    
                    