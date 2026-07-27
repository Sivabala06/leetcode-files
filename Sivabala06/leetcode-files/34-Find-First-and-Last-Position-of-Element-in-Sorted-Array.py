class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        
        k=[-1,-1]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                if nums[mid]==nums[mid+1]:
                    return [mid,mid+1]
                elif nums[mid]==nums[mid-1]:
                    return [mid-1,mid]
            if target>nums[mid]:
                l=mid+1
            else :
                r=mid-1
        return k


        