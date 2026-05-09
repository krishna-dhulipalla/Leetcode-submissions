class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # kth largest = (n-k)th smallest

        def quickselect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                return quickselect(p + 1, r)
            else:
                return quickselect(l, p - 1)

        return quickselect( 0, len(nums) - 1)