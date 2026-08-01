class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [1,2,3,4,5,6,7,8]
        # # target
        ptr1 = 0
        ptr2 = len(numbers) - 1

        while ptr1 <= ptr2:
            currAdd = numbers[ptr1] + numbers[ptr2]
            if currAdd == target:
                return [ptr1 + 1, ptr2 + 1]
            elif currAdd > target:
                ptr2 -= 1
            else:
                ptr1 += 1
            