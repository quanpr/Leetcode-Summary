class Solution:
    # the idea is that each operator seperates the string as the left part and right part.
    # Each part can be regard as a subproblem of the original question. After solving each 
    # subproblem, combine them together.
    # Divide & Conquer:
    # 1) divde the problem as a subproblem
    # 2) merge subproblem together
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        oper = {}
        oper['*'] = lambda x,y: x*y
        oper['+'] = lambda x,y: x+y
        oper['-'] = lambda x,y: x-y
        if input.isdigit():
            return [int(input)]
        
        res = []
        for i in range(len(input)):
            if input[i] in oper:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                #print(left, right)
                for res1 in left:
                    for res2 in right:
                        res.append(oper[input[i]](res1, res2))
        return res
                    