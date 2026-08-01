class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: #If the number we add is bigger its the only that matters
                q.pop()
            q.append(r)
            if q[0] <= r - k:
                q.popleft()
            if r + 1 >= k:
                res.append(nums[q[0]])
            r += 1

        return res

