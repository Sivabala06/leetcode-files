class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ress={}
        for i in nums:
            if i in ress:
                return True
            ress[i]=1
        return False