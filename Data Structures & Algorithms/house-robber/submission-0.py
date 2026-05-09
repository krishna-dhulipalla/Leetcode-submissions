class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2, prev1 = 0, 0   # dp[i-2], dp[i-1]

        for num in nums:
            curr = max(prev1, num + prev2)
            prev2, prev1 = prev1, curr

        return prev1
