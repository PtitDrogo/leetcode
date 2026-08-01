class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        m = 0
        res = []
        nums = sorted(nums)
        print(nums)
        while m < (len(nums) - 2):
            m += 1
            l = m - 1
            r = m + 1
            while l >= 0 and r <= len(nums) - 1:
                print([nums[l], nums[m], nums[r]])
                currAdd = nums[l] + nums[m] + nums[r]
                if currAdd == 0:
                    if [nums[l], nums[m], nums[r]] not in res:
                        res.append([nums[l], nums[m], nums[r]])
                    if l > 0:
                        l -= 1
                    elif r < len(nums) - 1:
                        r += 1
                    else:
                        break
                elif currAdd > 0:
                    l -= 1
                else:
                    r += 1
        return res
