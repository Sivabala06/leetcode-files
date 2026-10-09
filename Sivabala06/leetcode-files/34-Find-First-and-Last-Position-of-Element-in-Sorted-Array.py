class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        k=[-1,-1]
        # if len(nums)==1:
        #     if target != nums[0]:
        #         return k
            
        # if len(nums)==2:
        #     if nums[0]==nums[1]:
        #         return [0,1]
        #     return [0,0]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=ans2=ans3=mid
                while l<=r:
                    l=mid-1
                    mid=(l+r)//2
                    if nums[mid]==target:
                        ans2=mid
                    r=mid-1
                while l<=r:
                    r=mid+1
                    mid=(l+r)//2
                    if nums[mid]==target:
                        ans3=mid
                    l=mid+1
                return [ans2,ans3]
                    
            if target>nums[mid]:
                l=mid+1
            else :
                r=mid-1
        return k

        # if target in nums:
        #     try:
        #         d = nums.index(target)
        #         print(nums[d])  
        #     except ValueError:
        #         print(f"{target} is not in the list!")
        #     if nums[d]==nums[d+1]:
        #         return [d,d+1]
        #     elif nums[d]==nums[d-1] :
        #         return [d-1,d]
        # return [-1,-1]
                
        