class Solution:
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dum = []
        res = []
        # def solve(start,curr,res,nums,t):
        #     if t<0:
        #         return 
        #     if t==0:
        #         res.append(curr.copy())
        #         return
            
        #     for i in range(start,len(nums)):
        #         curr.append(nums[i])
        #         solve(i,curr,res,nums,t-nums[i])
        #         curr.pop()
        # solve(0,curr,res,nums,target)
        # return res
        def slove(start,r):
            if r<0:
                return
            if r == 0:
                res.append(dum.copy())
                return

            for i in range(start,len(nums)):
                dum.append(nums[i])
                slove(i,r - nums[i])
                dum.pop()

        slove(0,target)
        return res


    