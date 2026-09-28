class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        m=min(nums)
        g=nums.index(m)
        print(g)
        print(len(nums))
        if g == (len(nums)-1):
            return 0
        me=max(nums[g:])
        return me-m
        