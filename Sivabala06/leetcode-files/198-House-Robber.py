class Solution:
    def rob(self, nums: List[int]) -> int:
        # n=len(nums)
        # # lsum=0
        # # rsum=0
        # # for i in range(0,n):
        # #     if i%2==0 or i==0:
        # #         lsum+=nums[i]
        # #     elif i%2 !=0:
        # #         rsum+=nums[i]
            
        # # return max(lsum,rsum,n)
        # dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=nums[0]
        # for i in range(1,n):
        #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        # return dp[n]
      
        di=[0]*len(nums)
        
        di[0]=nums[0]
        if len(nums)<2:
            return max(di)
        di[1]=nums[1]
        if len(nums)<=2:
            return max (di)
        for i in range(1,len(nums)):
            di[i]=max(nums[i]+di[i-2],di[i-1])
        return max(di)

        