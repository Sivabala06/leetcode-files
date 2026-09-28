class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        # m=min(nums)
        # g=nums.index(m)
        # me=max(nums[g:])
        # return me-m
        mins=nums[0]
        mp=0
        for i in range(1,len(nums)):
            if nums[i]<mins:
                mins=nums[i]
            cp=nums[i]-mins
            if(cp>mp):
                mp=cp
        return mp