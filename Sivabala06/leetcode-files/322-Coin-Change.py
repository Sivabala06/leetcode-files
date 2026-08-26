class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        def ash(t):

            if t == 0:
                return 0

            best = float('inf')

            for i in range(len(coins) - 1, -1, -1):

                if t >= coins[i]:

                    r = t - coins[i]

                    result = ash(r)

                    best = min(best, 1 + result)

            return best

        ans = ash(amount)

        if ans == float('inf'):
            return -1

        return ans