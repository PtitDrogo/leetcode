class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            toSearch = target - nums[i]
            if toSearch in myMap:
                return [myMap[toSearch], i]
            myMap[nums[i]] = i
        return [-1, -1]