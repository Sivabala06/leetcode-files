class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n)
        dp[0]=nums[0]
        if n<2:
            return max(dp)
        
        dp[1]=nums[1]
        if n<=2:
            return max(dp)
        for i in range(1,n):
            if i==n-1 and n%2!=0:
                dp[i]=max(dp[i-1],dp[i-2]+nums[i]-dp[0])
                break
            if i==n-1 and n%2==0:
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
                break
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return max(dp)


        
        