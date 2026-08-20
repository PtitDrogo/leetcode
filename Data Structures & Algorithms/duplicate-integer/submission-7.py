class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = defaultdict(int)
        for n in nums:
            if myDict[n]:
                return True
            myDict[n] = 1
        return False