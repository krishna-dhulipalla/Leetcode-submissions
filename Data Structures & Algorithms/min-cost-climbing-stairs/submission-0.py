class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x, y = 0, 0

        for i in range(len(cost) - 1, -1, -1):
            cost[i] = min(cost[i] + x , cost[i] + y)
            x, y = cost[i], x
        return min(cost[0], cost[1])