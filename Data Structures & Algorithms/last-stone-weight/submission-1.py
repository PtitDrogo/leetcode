class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 != stone2:
                # -10 - -15 = -5
                # 15 - 10 = 5
                new_stone = -abs(stone1 - stone2)
                heapq.heappush(heap, new_stone)
        if heap:
            return -heap[0]
        return 0
            