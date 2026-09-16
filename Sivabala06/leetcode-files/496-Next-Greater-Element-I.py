class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums1)
        m=len(nums2)
        dp=[-1]*n
        
        for i in range(n):
            j=nums2.index(nums1[i])
            for k in range(j+1,m):
                if nums2[k]>nums2[j]:
                    dp[i]=nums2[k]
                    break
            

        return dp




        