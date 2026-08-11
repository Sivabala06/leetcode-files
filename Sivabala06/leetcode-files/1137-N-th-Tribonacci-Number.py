class Solution:
    def tribonacci(self, n: int) -> int:
        #bottom up approach
        # if n==0:
        #     return 0
        # if n<=2:
        #     return 1
        # dp=[0]*(n+1)
        # print(dp)
        # dp[0]=0
        # dp[1]=1
        # dp[2]=1
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        # return dp[-1]



        #top down approach:
        def tfib(n,m):
            if n in m:
                return m[n]
            if n == 0:
                return 0
            if n<=2:
                return 1
            m[n]=tfib(n-1,m)+tfib(n-2,m)+tfib(n-3,m)
            return m[n]

        return tfib(n,{})


        