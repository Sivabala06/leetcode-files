class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        dp = {}

        def ash(t):

            if t == 0:
                return 0

            if t in dp:
                return dp[t]

            best = float('inf')

            for i in range(len(coins) - 1, -1, -1):

                if t >= coins[i]:

                    r = t - coins[i]

                    result = ash(r)

                    best = min(best, 1 + result)

            dp[t] = best

            return dp[t]

        ans = ash(amount)

        if ans == float('inf'):
            return -1

        return ans