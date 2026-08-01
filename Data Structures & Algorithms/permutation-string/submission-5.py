class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        myMap = defaultdict(int)

        for c in s1:
            myMap[c] += 1
        print(myMap)

        l = 0
        r = len(s1) - 1
        
        while r in range(len(s2)):
            currMap = defaultdict(int)
            j = l
            while j <= r:
                currMap[s2[j]] += 1
                j += 1
            if myMap == currMap:
                return True
            print(currMap)
            print("VS")
            print(myMap)
            l += 1
            r += 1

        return False