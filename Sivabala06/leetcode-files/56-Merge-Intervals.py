class Solution:
    def merge(self, ins: list[list[int]]) -> list[list[int]]:
        ins.sort()
        bas=ins[0]
        
        if len(ins)==1:
            return ins
        res=[]
        for i in ins[1:]:
            
            if i[0]<=bas[1] :
                
                bas[1]=max(i[1],bas[1])
            else:
                res.append(bas)
                bas=i
        res.append(bas)
        
        return res

        