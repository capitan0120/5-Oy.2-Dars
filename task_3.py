from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-2], cost[i-1]) + cost[i]
        return min(cost[-2], cost[-1])

obj = Solution()
print(obj.minCostClimbingStairs(cost=[1,100,1,1,1,100,1,1,100,1]))
print(obj.minCostClimbingStairs(cost=[10,15,20]))
print(obj.minCostClimbingStairs(cost=[0,2,2,1]))
print(obj.minCostClimbingStairs(cost=[0,1,2,0]))