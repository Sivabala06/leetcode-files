class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=0
        maxs=[]
        sums=0
        while(right<len(nums)):
            sums+=nums[right]
            
            if (right-left+1)==k:
                maxs.append(sums/k)
                sums-=nums[left]
                left+=1
            right+=1
        return max(maxs)
                
            

           
            