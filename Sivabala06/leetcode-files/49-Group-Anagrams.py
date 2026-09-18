class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        cop=[]
        ans=[]
        
        
        for i in strs:
            j="".join(sorted(i))
            cop.append(j)
        kop=list(set(cop))
         
            
        for i in range(len(kop)):
            res=[]
            c=0
            for j in range(len(cop)):
                if kop[i]==cop[j]:
                    res.append(strs[j])
                 
            ans.append(res)
            
                    
            
       
            
        


        return  ans   
            








        