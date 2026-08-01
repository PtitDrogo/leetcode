class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, value in enumerate(nums):
            mydict[value] = i
        print(mydict)
        for i in range(len(nums)):
            left = target - nums[i]
            print(left)
            if mydict.get(left, None) != None and mydict.get(left, None) != i:
                return [i, mydict[left]]
        return [-1, -1]