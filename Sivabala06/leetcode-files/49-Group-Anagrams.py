class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # cop=[]
        # ans=[]
        # for i in strs:
        #     j="".join(sorted(i))
        #     cop.append(j)
        # kop=list(set(cop))    
        # for i in range(len(kop)):
        #     res=[]
        #     c=0
        #     for j in range(len(cop)):
        #         if kop[i]==cop[j]:
        #             res.append(strs[j])  
        #     ans.append(res) 
        # return  ans   
            
        grp={}

        for w in strs:
            key="".join(sorted(w))

            if key not in grp:
                grp[key]=[]
            grp[key].append(w)

        return list(grp.values())
            







        