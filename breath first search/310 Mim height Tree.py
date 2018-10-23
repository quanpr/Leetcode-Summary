# The idea is to trim every leaf in one iteration
# until there is 1 or 2 leaves left. Then the left leaves
# are solutions. 
#
# When trimming a leaf, we first remove it from its adjacent node.
# During that iteration, some nodes will become new leaves, since 
# a tree must has node that is not branched at all. Pruning leaves
# won't change a tree to other structures.

from collections import deque
class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n ==1: return [0]
        graph = [[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        leaves = [i for i in range(n) if len(graph[i])==1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j])==1:
                    newLeaves.append(j)
            leaves=newLeaves
        return leaves
        
        