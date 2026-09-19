class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        k=1
        if 0 in nums:
            j=nums.index(0)
            h=nums.copy()
            h.remove(0)
            for i in h:
                k*=i
            g=[0]*len(nums)
            g[j]=k
            return g

        for i in nums:
            k*=i
        g=[k]*len(nums)
        return [g[i]//nums[i] for i in range(len(nums))]
        
        