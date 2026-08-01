class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            currstr = str(len(s)) + "#" + s
            encodedStr += currstr
        print(encodedStr)
        return encodedStr


    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i = 0
        while i in range(len(s)):
            start = i
            #get the number of characters:
            wordSize = ""
            print("at start i is", i)
            while s[start].isdigit() and s[start] != "#":
                wordSize += s[start]
                start += 1
            print("the wordsize i got is : ", wordSize)
            #We are now on the # symbol
            start += 1
            print("start is :", start)
            currStr = s[start:start + int(wordSize)]
            decodedStr.append(currStr)
            i += int(wordSize) + 1 + len(wordSize)
        return decodedStr




#I can either do an escape character for a delimiter 
#or I do the thing with the # and the number
