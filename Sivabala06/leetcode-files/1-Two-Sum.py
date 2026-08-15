class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # l=0
        # h=[]
        # r=len(nums)-1
        # while (l<=r):
        #     sum1=nums[l]+nums[r]
        #     if sum1==target:
        #         h=[l,r]
        #         return h
        #         break
        #     elif sum1<target:
        #         l+=1
        #     elif sum1>target:
        #         r-=1
        res={}
        for i in range(len(nums)):
            r=target-nums[i]
            if r in res:
                return [nums.index(r),i]
            res[nums[i]]=i

