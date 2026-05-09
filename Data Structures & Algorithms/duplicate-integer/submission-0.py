class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()

        for i in nums:
            if i not in hashMap:
                hashMap.add(i)
            else:
                return True
        
        return False