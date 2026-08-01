class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        i = 0
        startIndex = len(nums) - 1
        endIndex = 0
        maxTmp = -1001
        addtmp = 0

        while i in range(len(nums)):
            addtmp += nums[i]
            if addtmp >= maxTmp:
                maxTmp = addtmp
                endIndex = i
            i += 1

        #second pass
        i = len(nums) - 1
        maxTmp = -1001
        addtmp = 0
        while i >= 0:
            addtmp += nums[i]
            if addtmp >= maxTmp:
                maxTmp = addtmp
                startIndex = i
            i -=1
        
        oopsallnegative = True
        for n in nums:
            if n > 0:
                oopsallnegative = False
                break
        if oopsallnegative == True:
            return max(nums)


        print(f"startIndex = {startIndex}, endIndex = {endIndex}")
        return sum(nums[startIndex:endIndex + 1])
            

