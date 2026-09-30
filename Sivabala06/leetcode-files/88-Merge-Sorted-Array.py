class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        # nums=nums1[:m]
        # nums3=nums2[:n]
        nums1[:]=nums1[:m]+nums2[:n]
        print(nums1.sort())

    
