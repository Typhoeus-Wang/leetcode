class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        left = 0
        
        # expand the window
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update the result
                if (right - left + 1) < resLen:
                    res = s[left:right + 1]
                    resLen = min(resLen, right - left + 1)
                
                # shrink the window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        return res if resLen != float("inf") else ""