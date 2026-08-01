class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #I will make two pointers.
        #if numbers[l] + numbers[r] > target, then it means we need a lower number, so we move r
        #and vice versa.

        r = len(numbers) - 1
        l = 0
        while l < r:
            curr = numbers[r] + numbers[l]
            print(curr)
            if curr == target:
                return [l + 1, r + 1]
            elif curr > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]

        