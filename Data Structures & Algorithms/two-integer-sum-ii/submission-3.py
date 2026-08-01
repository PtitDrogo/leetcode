class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) - 1
        start = 0        
        while start <= end:
            if numbers[start] + numbers[end] == target:
                res = []
                res.append(start + 1)
                res.append(end + 1)
                return res
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
        res = [0]
        return res

        