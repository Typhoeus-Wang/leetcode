class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def stackProcess(s):
            res = []
            for char in list(s):
                if char == "#":
                    if len(res) != 0:
                        res.pop()
                else:
                    res.append(char)
            return ''.join(res)


        def twoPointersProcess(s):
            slow, fast = 0, 0
            s = list(s)
            while fast < len(s):
                if s[fast] != "#":
                    s[slow] = s[fast]
                    fast += 1
                    slow += 1
                else:
                    if slow != 0:
                        slow -= 1
                    fast += 1
            return ''.join(s[:slow])

        processed_s = stackProcess(s)
        processed_t = stackProcess(t)
        print(processed_s)
        print(processed_t)
        return processed_s == processed_t