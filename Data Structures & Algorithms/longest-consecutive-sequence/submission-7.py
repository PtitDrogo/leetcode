class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        
        if not nums:
            return 0
        res = 1;
        #I want to iterate through my list, i then check if that num -1 exist in the set
        for num in mySet:
            if num - 1 not in mySet:
                tmp = num + 1
                currentStreak = 1
                while tmp in mySet:
                    currentStreak += 1
                    tmp = tmp + 1
                res = max(currentStreak, res)
        return res

