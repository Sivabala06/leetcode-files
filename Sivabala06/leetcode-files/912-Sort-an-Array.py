class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merges(nums):
            if len(nums)>1:
                mid=(len(nums)//2)
                left = nums[:mid]
                right=nums[mid:]

                merges(left)
                merges(right)

                lp=0
                rp=0
                fp=0
                
                while lp<len(left) and rp<len(right):
                    if left[lp]<right[rp]:
                        nums[fp]=left[lp]
                        lp+=1
                    else:
                        nums[fp]=right[rp]
                        rp+=1
                    fp+=1
                while lp<len(left):
                    nums[fp]=left[lp]
                    lp+=1
                    fp+=1
                while rp<len(right):
                    nums[fp]=right[rp]
                    rp+=1
                    fp+=1
            return nums
        k=merges(nums)
        return nums



                    

        