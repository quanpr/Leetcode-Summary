from copy import deepcopy
import sys
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(graph, idx, aux, res, past, maxLen):
            x, y = idx[0], idx[1]
            m, n = len(graph), len(graph[0])
            
            if idx[0] < 0 or idx[0] >= m or idx[1] < 0 or idx[1] >= n or graph[x][y]=='x' or graph[x][y] <= past: 
                if len(aux) > maxLen[0]:
                    res.append(len(aux))
                    maxLen[0] = len(aux)

            else:
                cur = graph[x][y]
                graph[x][y] = 'x'
                aux.append(cur)
                dfs(graph, (idx[0]-1,idx[1]), aux[:], res, cur, maxLen)
                dfs(graph, (idx[0],idx[1]-1), aux[:], res, cur, maxLen)
                dfs(graph, (idx[0],idx[1]+1), aux[:], res, cur, maxLen)
                dfs(graph, (idx[0]+1,idx[1]), aux[:], res, cur, maxLen)
                graph[x][y] = cur
        
        
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        res, maxLen = [], [0]
        dfs(matrix, (2,1), [], res, -sys.maxsize, [0])
        
        for i in range(m):
            for j in range(n):
                dfs(matrix[:], (i,j), [], res, -sys.maxsize, [0])
                
        return max(res)