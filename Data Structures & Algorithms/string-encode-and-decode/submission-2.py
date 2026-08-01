class Solution:

    def encode(self, strs: List[str]) -> str:
        decodedStr = ""
        for s in strs:
            decodedStr += str(len(s)) + "#" + s
        return decodedStr

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i in range(len(s)):
            j = i
            while s[i] != "#":
                i += 1
            j = int(s[j:i])
            i += 1
            res.append(s[i:i + j])
            i += j
        return res




#Trying to solve this with just a delimiter to see why not.
#we just say that \ is the escape character, unless its followed
#by another \, then we cancel one