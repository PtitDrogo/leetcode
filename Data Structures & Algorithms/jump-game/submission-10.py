#I want to have my guy jump, and eventually the best jump
#will either lead to the end or lead to a 0.
#[4,3,2,10,1,0,0,0] 
#[4,3,2,1,0]
# nums[i] + i
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while True:
            bestJump = 0
            bestJumpIndex = 0
            if (nums[i] + i) >= len(nums) - 1:
                return True
            if (nums[i] == 0):
                return False
            for j in range(nums[i] + 1):
                currJump = nums[i + j] + j
                if (currJump >= bestJump):
                    bestJump = currJump
                    bestJumpIndex = j
            i += bestJumpIndex