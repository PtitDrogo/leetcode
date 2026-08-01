class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #I had the correct logic, just some things that probably made it wrong
        #1. Storing the need = have instead of comparing everytime
        #2. Looping constantly with l instead of doing it once per loop

        count = defaultdict(int)
        new_count = defaultdict(int)
        res, resLen = "", float("infinity")
        l = 0
        if len(s) < len(t) or t == "":
            return ""

        for c in t:
            count[c] += 1
        have, need = 0, len(count)
        for r in range(len(s)):
            c = s[r]
            new_count[c] += 1
            if c in count and count[c] == new_count[c]:
                have += 1
            while have == need:
                c = s[l]
                if len(s[l:r+1]) < resLen:
                    res = s[l:r + 1]
                    resLen = len(s[l:r+1])
                new_count[c] -= 1
                if c in count and new_count[c] < count[c]:
                    have -= 1
                l += 1
        return res if resLen != float("infinity") else ""