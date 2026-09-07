# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         l=nums.index(min(nums))
#         r=nums.index(max(nums))
#         g=1
#         for i in range(l,r):
#             if nums[i+1]>nums[i]:
#                 g+=1
#                 l+=1
#             else:
#                 pass
#         return g
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        r = len(nums) 
        dp=[1]*len(nums)
        for i in range(r):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp[i]=max(dp[i],dp[prev]+1)

        return max(dp)



        



        