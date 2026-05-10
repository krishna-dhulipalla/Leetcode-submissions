from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        countT, window = Counter(t), defaultdict(int)
        res, reslen = [-1, -1], float("infinity")
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            if ch in countT and countT[ch] == window[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = l, r
                    reslen = r - l + 1
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1]
