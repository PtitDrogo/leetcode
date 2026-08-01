class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        #Im using a heap to know where my smallest number is
        #But I will also needs its index to know if its in the window
        #Thus, im storing (index,value) tuples.
        #heapq.heappush()
        #heapq.heappop()
        #heapq.heapify()

        for i, n in enumerate(nums):
            #if the index isnt in i - k aka the window, we pop it.
            print(i)
            print(heap)
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)

            #We had our element to our q
            heapq.heappush(heap, (-n, i))

            #We add our smallest element to the result
            if i >= k - 1:
                res.append(heap[0][0] * -1)
        return res

