class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       
        res=[]
        dum=[]
        nums=[i+1 for i in range(n)]
        left=0
        while(left<len(nums)):
            dum.append(nums[left])
            def com(i):
                if len(dum)==k:
                    res.append(dum.copy())
                    return
                if i>=len(nums):
                    return
                
                     
                if len(dum) < k:
                    dum.append(nums[i])
                    com(i+1)
                    dum.pop()
                    com(i+1)
                
                
            com(left+1)
            dum=[]
            left+=1

        return res



        