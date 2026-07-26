class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        mi=0
        for i in range (len(nums)):
            if nums[i]%2 ==0 :
                nums[mi], nums[i] = nums[i], nums[mi]
                mi += 1
        return nums