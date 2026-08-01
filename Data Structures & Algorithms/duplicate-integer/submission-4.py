class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for n in nums:
            if m.get(n, None):
                return True
            else:
                m[n] = 1
        return False