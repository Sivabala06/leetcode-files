class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)-1
        for i in range(n):
            if nums[i]==target :
                return i
            elif nums[i] < target and nums[i+1]>=target:
                return i+1
        if nums[n] < target :
            return len(nums)
        else:
            return 0

          
        