class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count =0
        # candidate=None
        # for num in nums:
        #     print(candidate)
        #     if count==0:
        #         candidate=num
        #     if num==candidate:
        #         count+=1
        #     else:
        #         count-=1
        # return candidate
        counter={}
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        k=max(counter,key=counter.get)
        return k