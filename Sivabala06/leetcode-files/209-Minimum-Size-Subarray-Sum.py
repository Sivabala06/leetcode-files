class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        mins =100000000000
        subsum=0
        while(right<len(nums)):
            subsum+=nums[right]
            while subsum >= target:
                mins=min(mins,right-left+1)
                subsum-=nums[left]
                left+=1
            right+=1

        return 0 if mins==100000000000 else mins