class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #coding a non optimal solution i guess
        res = []

        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            days = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > currTemp:
                    days = j - i
                    break
            res.append(days)
        return res