class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n,dp):
            if n in dp:
                return dp[n]
            if n == 1:
                return 1
            if n ==2:
                return 2
           
            dp[n]=climb(n-1,dp)+climb(n-2,dp)

            return dp[n]

        
        return climb(n,{})
            
        