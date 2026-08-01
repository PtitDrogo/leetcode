[10,1,0]

class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jumpCount = 0
        # count = 0
        while goal > 0:
            bestJumpIndex = 101
            for i in range(goal - 1, -1, -1):
                currJump = nums[i] + i
                print(f" - currjump : {currJump} vs goal : {goal} vs bestJumpIndex: {bestJumpIndex}")
                if (currJump >= goal and i < bestJumpIndex):
                    bestJumpIndex = i
            goal = bestJumpIndex
            jumpCount += 1
            # count += 1
            print(f"hello, goal is {goal}, jumpcount is {jumpCount}")
            # if count >= 12:
            #     return jumpCount
        return jumpCount

            