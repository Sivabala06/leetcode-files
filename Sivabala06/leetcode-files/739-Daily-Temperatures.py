class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[0]*n
        stack = []
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                j = stack.pop()
                dp[j] = i - j

            stack.append(i)
        return dp

                
                
           
        