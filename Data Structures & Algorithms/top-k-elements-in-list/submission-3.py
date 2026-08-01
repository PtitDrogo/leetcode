class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        myMap = defaultdict(int)

        for n in nums:
            myMap[n] += 1
        res = []
        for key in myMap:
            iterations = myMap[key]
            buckets[iterations].append(key)   
        for bucket in reversed(buckets):
            for n in bucket:
                k -= 1
                res.append(n)
                if k <= 0:
                    return res   
        return res