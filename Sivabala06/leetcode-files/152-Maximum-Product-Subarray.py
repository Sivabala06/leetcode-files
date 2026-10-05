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
        # if len(nums)<2:
        #     return nums[0]
        
        
        # dp=nums[0]
        # m2=m1=1
        
        # for i in range(len(nums)):
             
        #     val=(nums[i],nums[i]*m1,nums[i]*m2)
        #     m1,m2=max(val),min(val)
        #     dp=max(dp,m1)

        # return dp


        if not nums:
            return 0
        
        n = len(nums)
        dp = [0] * n
        
        # m1 tracks the max product ending at the current position
        # m2 tracks the min (most negative) product ending at the current position
        m1 = nums[0]
        m2 = nums[0]
        dp[0] = nums[0]
        
        for i in range(1, n):
            curr = nums[i]
            
            # Save previous m1 before updating it, 
            # because m2 needs the old m1 to calculate correctly!
            prev_m1 = m1
            
            m1 = max(curr, prev_m1 * curr, m2 * curr)
            m2 = min(curr, prev_m1 * curr, m2 * curr)
            
            # Store the max result at this step in your dp array
            dp[i] = m1
            
        return max(dp)

            

            

            
            



        