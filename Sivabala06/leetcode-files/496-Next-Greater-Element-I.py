class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums1)
        m=len(nums2)
        dp=[-1]*n
        
        # for i in range(n):
        #     j=nums2.index(nums1[i])
        #     for k in range(j+1,m):
        #         if nums2[k]>nums2[j]:
        #             dp[i]=nums2[k]
        #             break

        # return dp

        stack=[]
        b = {}

        for j in range(len(nums2)):
            while stack and nums2[j] > nums2[stack[-1]]:
                k = stack.pop()
                b[nums2[k]] = nums2[j]

            stack.append(j)

        for i in range(len(nums1)):
            dp[i] = b.get(nums1[i], -1)
        return dp



        