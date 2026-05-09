class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        HashMap = set(nums)
        longest_sequence = 0

        for i in nums:
            if i-1 not in HashMap:
                j = i
                sequence_len = 1
                while j+1 in HashMap:
                    sequence_len += 1
                    j+=1
                longest_sequence = max(longest_sequence, sequence_len)

        return longest_sequence