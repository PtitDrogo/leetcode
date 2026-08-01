class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        firstWord = strs[0]
        for i in range(len(firstWord)):
            curr = firstWord[i]
            for s in strs:
                if i > len(s) - 1 or s[i] != curr:
                    return res
            res += curr
        return res