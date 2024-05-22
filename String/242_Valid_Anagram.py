class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # edge case
        if len(s) != len(t):
            return False
        
        record = [0] * 26
        for c in s:
            record[ord(c) - ord('a')] += 1
        for c in t:
            record[ord(c) - ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True