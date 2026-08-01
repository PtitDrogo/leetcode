class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        power = 0
        bestStationIndex = -1
        while i < len(gas):
            power += gas[i] - cost[i]
            if power < 0:
                bestStationIndex = -1
            if gas[i] - cost[i] >= 0 and bestStationIndex == -1:
                bestStationIndex = i
            i += 1
        if power < 0:
            return -1
        return bestStationIndex