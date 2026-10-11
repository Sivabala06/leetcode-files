class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        
        # n=len(nums)
        # ls=0
        # rs=0
        # for i in range(n):
        #     ls=sum(nums[:i])
        #     rs=sum(nums[i:]) -nums[i]
        #     if (rs==ls):
        #         return i
        # return -1
        n=len(nums)
        ls=[0]*n
        rs=[0]*n
        if n==1:
            return 0
        ls[1]=nums[0]
        for i in range(2,n):
            ls[i]=ls[i-1]+nums[i-1]
        rs[n-2]=nums[n-1]
        for i in range(n-3,-1,-1):
            rs[i]=nums[i+1]+rs[i+1]

        for i in range(n):
            if rs[i]==ls[i]:
                return i
        return -1
            
        