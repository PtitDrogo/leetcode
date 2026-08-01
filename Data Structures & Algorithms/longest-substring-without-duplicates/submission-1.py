class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        i = 0
        maxLen = 0

        for i in range(len(s)):
            currMap = defaultdict(int)
            while i in range(len(s)):
                print("hi")
                currMap[s[i]] += 1
                if currMap[s[i]] > 1:
                    break
                i += 1
            maxLen = max(len(currMap), maxLen)
        return maxLen



                
            