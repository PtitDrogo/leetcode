from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        new_count = defaultdict(int)
        res = ""  # Change 1: Initialize as empty
        l = r = 0
        if len(s) < len(t):
            return ""

        for c in t:
            count[c] += 1
        print(count)

        while r < len(s):
            #I only want to add stuff if its in t
            substring = s[l:r + 1]
            print(f"substring = {substring}")
            print(f"new_count = {new_count}")
            if s[r] in t:
                new_count[s[r]] += 1
            while self.compareDict(count, new_count):
                substring = s[l:r + 1]
                if not res or len(substring) < len(res):  # Change 2: Check if res is empty first
                    res = substring
                if s[l] in t:  # Change 3: Only decrement if character is in t
                    new_count[s[l]] -= 1
                l += 1
            r += 1
        return res

    def compareDict(self, s: defaultdict, t: defaultdict) -> bool:
        for key in s.keys():
            if s[key] > t[key]:
                return False
        return True