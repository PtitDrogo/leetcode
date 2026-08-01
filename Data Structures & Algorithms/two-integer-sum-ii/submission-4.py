class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) - 1
        start = 0        
        while start <= end:
            curSum = numbers[start] + numbers[end]
            if curSum == target:
                return [start + 1, end + 1]
            if curSum > target:
                end -= 1
            elif curSum < target:
                start += 1
        res = [0]
        return res

        