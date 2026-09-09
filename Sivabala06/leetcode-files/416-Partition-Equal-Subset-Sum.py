class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        i=len(nums)//2
        s1=nums[:i]
        s2=nums[i:]
        while(len(s1)>1 and len(s2)>1):
            if sum(s1)<sum(s2):
                m=min(s2)
                s2.remove(m)
                s1.append(m)
            if sum(s1)==sum(s2):
                return True
                
        return False
                
                




        