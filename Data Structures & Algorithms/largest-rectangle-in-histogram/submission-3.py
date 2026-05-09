class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []  

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                p, height = stack.pop()
                area = max(area, height * (idx - p))
                start = p 
            stack.append((start, h))

        n = len(heights)
        while stack:
            p, h = stack.pop()
            area = max(area, h * (n - p))

        return area