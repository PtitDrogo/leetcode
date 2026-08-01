class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) - 1
        start = 0;

        while start <= end:
            mySum = numbers[start] + numbers[end]
            if mySum > target:
                end -= 1
            elif mySum < target:
                start += 1
            else:
                return [start + 1, end + 1]

        