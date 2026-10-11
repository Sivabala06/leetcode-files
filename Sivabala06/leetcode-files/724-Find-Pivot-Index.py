class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        ls=0
        rs=0
        for i in range(n):
            ls=sum(nums[:i])
            rs=sum(nums[i:]) -nums[i]
            if (rs==ls):
                return i
        return -1