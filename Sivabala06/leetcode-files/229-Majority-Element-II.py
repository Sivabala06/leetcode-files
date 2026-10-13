class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count={}
        maxi=abs(len(nums)/3)
        for i in nums:
            if i not in count:
                count[i]=0
            count[i]+=1
        result = [key for key,val in count.items() if val > maxi]
        return result


        