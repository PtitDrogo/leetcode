class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for s in strs: #strings in given list
            found = False
            for l in res: #lists in res
                if self.areAnagrams(s, l[0]):
                    print("anagram found")
                    l.append(s)
                    found = True
                    break
            if found == False:
                res.append([s])
                
            
        return res

    def areAnagrams(self, s1: str, s2: str) -> bool:
        print(f"comparing {s1} and {s2}")
        if len(s1) != len(s2):
            return False
        count1, count2 = {}, {}
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0) 
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
        return count1 == count2