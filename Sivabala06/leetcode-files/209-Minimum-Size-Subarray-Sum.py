class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        mins =[]
        subsum=0
        while(right<len(nums)):
            subsum+=nums[right]
            while subsum >= target:
                mins.append(right-left+1)
                subsum-=nums[left]
                left+=1
            right+=1

        return 0 if len(mins)==0 else min(mins)