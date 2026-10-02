class Solution:
    def generate(self, n: int) -> list[list[int]]:
        if n==0 :
            return [[]]
        res=[[1]]
        
        for i in range(1,n):
            prev=res[-1]
            new=[1]

            for j in range(1,len(prev)):
                new.append(prev[j-1]+prev[j])

            new.append(1)
            res.append(new)
       
        return res