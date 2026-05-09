class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, i in enumerate(temperatures):
            while stack and i > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = idx - stackInd
            stack.append((i, idx))
        
        return res
