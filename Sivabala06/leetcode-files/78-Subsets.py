class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        dum=[]
        def back(j):
            if j == len(nums):
                res.append(dum.copy())
                return

            # TAKE nums[j]
            dum.append(nums[j])
            back(j + 1)
            dum.pop()

            # DON'T TAKE nums[j]
            back(j + 1)

        back(0)

        return res
                    
                
                
                
            
            
            
        