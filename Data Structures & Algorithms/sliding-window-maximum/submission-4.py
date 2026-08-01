class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        r = l = 0
        #We add to the right and remove to the right for the size of the value
        #For popping if not in window, we pop to the left
        #This preserve the order of insertion so to speak
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop() # we only care if the number is bigger
            q.append(r)
            #I only add to res if the window is big enough
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            #removing if not in window
            if l > q[0]:
                q.popleft()
            r += 1
        return res

