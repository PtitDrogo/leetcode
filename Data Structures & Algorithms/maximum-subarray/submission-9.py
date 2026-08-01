class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = -1
        #I want to advance and add the numbers
        #If at some point I go below 0, well I can just
        #reset to 0, this gets rid of the useless subarray essentially

        for n in nums:
            currSum += n
            maxSum = max(currSum, maxSum)
            currSum = max(currSum, 0)
        return maxSum


