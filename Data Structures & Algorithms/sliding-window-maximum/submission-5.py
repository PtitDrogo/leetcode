class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        #In my heap i will store tuple (value, index)
        for i in range(len(nums)):
            #Getting rid of values not in my window
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i], i))
            if i + 1 >= k:
                res.append(-heap[0][0])
        return res

