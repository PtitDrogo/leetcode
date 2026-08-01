from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_s = defaultdict(int)
        h_t = defaultdict(int)
        for letter in s:
            h_s[letter] += 1
        for letter in t:
            h_t[letter] += 1
        return (h_s == h_t)