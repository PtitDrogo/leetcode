class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #dumb ass fix so the equal sign works
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        myMap = defaultdict(int)
        currMap = defaultdict(int)
        #anton style fix
        if len(s1) > len(s2):
            return False
        for i in range(len(alphabet)):
            myMap[alphabet[i]] = 0
            currMap[alphabet[i]] = 0
        for c in s1:
            myMap[c] += 1
        l, r = 0, len(s1) - 1
        for i in range(len(s1)):
            currMap[s2[i]] += 1
        
        currMap[s2[r]] -= 1 
        while r in range(len(s2)):
            currMap[s2[r]] += 1   
            if myMap == currMap:
                return True
            print(currMap)
            print(myMap)
            currMap[s2[l]] -= 1
            l += 1
            r += 1
        return False   
        #this is correct but the syntax is fucking me since the default value
        #fuck with the = sign