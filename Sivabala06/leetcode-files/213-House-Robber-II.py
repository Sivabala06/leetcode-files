class Solution:
    def rob(self, nums: List[int]) -> int:
        # n=len(nums)
        # dp=[0]*(n)
        # dp[0]=nums[0]
        # if n<2:
        #     return max(dp)
        
        # dp[1]=nums[1]
        # if n<=2:
        #     return max(dp)
        # for i in range(1,n):
        #     if i==n-1 :
        #         dp[i]=max(dp[i-1],dp[i-2]+nums[i]-dp[0])
        #         break
        #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        # return max(dp)

        # see this is okay-- but our ultimate goal is to if we rob first house - dont rob last house-nad vice versa- then find 1st to n-1 and 2nd to n..find max)

        n=len(nums)
        if n==1:
            return nums[0]
        def solve(num):
            m=len(num)
            dp=[0]*m
            dp[0]=num[0]
            if m>1:
                dp[1]=max(num[0],num[1])
            for i in range(2,m):
                dp[i]=max(dp[i-1],dp[i-2]+num[i])
            return dp[-1]
        return max(solve(nums[1:]),solve(nums[:-1]))


        
        