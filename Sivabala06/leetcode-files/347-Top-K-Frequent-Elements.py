class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        kop=[]
        dic={}
        for i in nums:
            if i  not in dic:
                dic[i]=0
            dic[i]+=1
        print(dic)
        for i in range(k):
            maxs=max(dic,key=dic.get)
            kop.append(maxs)
            dic.pop(maxs,None)

        return kop


        