class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for idx, i in enumerate(nums):
            if i in diff:
                return [diff[i], idx]
            
            diff[target - i] = idx
