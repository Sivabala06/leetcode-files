
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # k=1
        # if 0 in nums:
        #     j=nums.index(0)
        #     h=nums.copy()
        #     h.remove(0)
        #     for i in h:
        #         k*=i
        #     g=[0]*len(nums)
        #     g[j]=k
        #     return g

        # for i in nums:
        #     k*=i
        # g=[k]*len(nums)
        # return [g[i]//nums[i] for i in range(len(nums))]


        # g=[1]*len(nums)
        # for i in range(len(nums)):
        #     if i==0:
        #         g[i]=math.prod(nums[i:])
        #     if i==len(nums)-1:
        #         g[i]=math.prod(nums[:i])
        #     g[i]=math.prod(nums[:i])* math.prod(nums[i+1:])
        # return g

        n = len(nums)
        g = [1] * n

        # Pass 1: product of everything to the LEFT
        left = 1
        for i in range(n):
            g[i] = left
            left *= nums[i]

        # Pass 2: product of everything to the RIGHT
        right = 1
        for i in range(n - 1, -1, -1):
            g[i] *= right
            right *= nums[i]

        return g
