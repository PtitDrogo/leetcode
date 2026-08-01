class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # return s == t
        m = {}
        m2 = {}
        for c in s:
            if m.get(c, None):
                m[c] += 1
            else:
                m[c] = 1
        for c in t:
            if m2.get(c, None):
                m2[c] += 1
            else:
                m2[c] = 1
        return m == m2