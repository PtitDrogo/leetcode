class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for cnt in count.values():
            heapq.heappush(maxHeap, -cnt)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) 
                #its +1 and not -1 because we have a negavive n in heap
                print(f"cnt = {cnt}")
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
