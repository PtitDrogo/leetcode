class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Input: nums = [1,2,1,0,4,2,6], k = 3
        l = 0
        r = k
        res = []
        while r <= len(nums):
            window = nums[l:r]
            print("window", window)
            res.append(max(window))
            l += 1
            r += 1
        return res