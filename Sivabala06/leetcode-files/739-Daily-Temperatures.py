class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[0]*n
        for i in range(n):
           if i== n-1:
            dp[i]=0
            break
           if nums[i+1]>nums[i]:
            dp[i]=1
           if nums[i]>nums[i+1]:
            dp[i]=1
            for j in range(i+1,n):
                if j==n-1 and nums[i]>nums[j]:
                    dp[i]=0
                    break
                if nums[i]>nums[j]:
                    dp[i]+=1
                    continue
                
                elif nums[i]<nums[j]:
                    break
        return dp
                
           
        