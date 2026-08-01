class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        list_of_hash_maps = []
        while strs:
            group = []
            group.append(strs[0])
            for i in range(1, len(strs)):
                if (self.isAnagram(strs[0], strs[i]) == True):
                    group.append(strs[i])
            list_of_hash_maps.append(group)
            for s in group:
                while s in strs:
                    strs.remove(s)
        return(list_of_hash_maps)
