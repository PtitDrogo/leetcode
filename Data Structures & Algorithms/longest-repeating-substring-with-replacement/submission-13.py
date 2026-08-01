class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myDict = {} #this will count the characters instances.
        res = 0
        l = 0
        for r in range(len(s)):
            myDict[s[r]] = 1 + myDict.get(s[r], 0)
            #if I still have a valid window, I extend r
            #if I dont have a valid window, I extend l until I do
            while (r - l + 1) - max(myDict.values()) > k:
                myDict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res



            
