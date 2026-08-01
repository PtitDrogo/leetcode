class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #n2 but oh well
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if (i != j):
                    product *= nums[j]
            res.append(product)
        return res
        
        
        
        
        # product = math.prod(nums)
        # res = []
        # for i in range(len(nums)):
        #     if (nums[i] == 0):
        #         num = 0
        #     else:
        #         num = product // nums[i]
        #     res.append(num)
        # return res