class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            width = 1
            left = i - 1
            right = i + 1
            while left >= 0 and heights[left] >= heights[i]:
                width += 1
                left -= 1
            while right < len(heights) and heights[right] >= heights[i]:
                width += 1
                right += 1
            area = max(area, width * heights[i])
        return area