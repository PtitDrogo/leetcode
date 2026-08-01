class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #I completely failed this, idk about bucket sort
        count = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        #Im creating a bucket for each number ig

        for num in nums:
            count[num] += 1
        for num, cnt in count.items():
            buckets[cnt].append(num)
        # the buckets are actually the bridge where well be able to have
        # a bucket for each possible counts (max being len(nums))
        
        res = []
        #this convoluted range function says to start at the end, stop at 0, and do
        # -1 each time
        #now, just starting with the buckets with most repetitions, i add
        #the frequency to the result list
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res