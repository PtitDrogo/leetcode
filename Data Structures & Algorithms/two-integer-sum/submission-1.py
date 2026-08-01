class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        #I get a number, whichs means I know the number that would do with it
        # (by doing target - number == number im looking for)
        # if I dont find it in my map, then I add it to the map and look at the next number
        # in the list
        for i in range(len(nums)):
            secondNum = target - nums[i]
            if secondNum in hashMap:
                return [hashMap[secondNum], i]
            else:
                hashMap[nums[i]] = i
        return [0,0]