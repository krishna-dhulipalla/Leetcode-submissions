class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in s:
            while right in seen:
                seen.remove(s[left])
                left += 1
            seen.add(right)
            max_len = max(len(seen), max_len)
        
        return max_len
                