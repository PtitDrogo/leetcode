class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)
        for n in nums:
            if m[n]:
                return True
            else:
                m[n] += 1
        return False