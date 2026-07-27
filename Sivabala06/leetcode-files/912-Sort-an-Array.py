import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quick(nums):
            if len(nums)<=1:
                return nums
            pivot=random.choice(nums)
            left=[i for i in nums if i<pivot]
            right=[i for i in nums if i>pivot]
            midd=[i for i in nums if i==pivot]
            return quick(left)+midd+quick(right)        
        return quick(nums)



                    

        