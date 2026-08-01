class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        res = 0

        if (len(height) == 1):
            return 0

        #i know
        while (height[l] == 0 and l in range(len(height))):
            l += 1
        if height[l] == 0:
            return 0
        
        while l in range(len(height)):
            r = l + 1
            if r not in range(len(height)):
                return res
            backupi = len(height) - 1
            while height[r] < height[l]:
                r += 1
                if r >= len(height):
                    break
                if (height[backupi] < height[r]):
                    backupi = r
            if r >= len(height) - 1:
                r = backupi
            pillar1 = min(height[backupi] ,height[l])
            l += 1
            print(r)
            while l < r:
                res += max(0, pillar1 - height[l])
                print(f"pillar1 = {pillar1}, height[l] = {height[l]}")
                print(f"l = {l}")
                print(f"res = {res}")
                l += 1
        return res