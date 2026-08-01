class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #All words are actually a tuple of how many of each char they have
        result = defaultdict(list)
        #the map will be a key thats count, a list of 26 numbers, and it will to a value
        # of a list of list, containing our word
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(word)
        return result.values()
