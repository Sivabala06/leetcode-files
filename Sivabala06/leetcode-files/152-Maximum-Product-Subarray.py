class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # left=0
        # right=1
        # maxi=nums[0]
        # w=nums[left]*nums[right]
        # while right<len(nums):
            
        #     if w>maxi:
        #         maxi=w
        #         right+=1
        #         w*=nums[right]
        #         continue
        #     w//=nums[left]
        #     left+=1
        # return maxi #-----------------wrongggggggggg--------
        if len(nums)<2:
            return nums[0]
        
        
        dp=nums[0]
        m2=m1=1
        
        for i in range(len(nums)):
             
            val=(nums[i],nums[i]*m1,nums[i]*m2)
            m1,m2=max(val),min(val)
            dp=max(dp,m1)




        return dp




            

            

            
            



        