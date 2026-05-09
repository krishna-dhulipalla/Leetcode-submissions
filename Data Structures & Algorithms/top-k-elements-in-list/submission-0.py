from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] += 1
        
        for key, value in count.items():
            frequency[value].append(key)
        
        res = []
        for i in range(len(frequency)-1, 0, -1):
            for j in frequency[i]:
                res.append(j)

                if k == len(res):
                    return res