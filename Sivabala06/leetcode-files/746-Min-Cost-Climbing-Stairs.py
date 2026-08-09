class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def climb(i, dp):
            if i >= len(cost):
                return 0

            if i in dp:
                return dp[i]

            dp[i] = cost[i] + min(
                climb(i+1, dp),
                climb(i+2, dp)
            )

            return dp[i]
        return min(climb(0,{}),climb(1,{}))




        