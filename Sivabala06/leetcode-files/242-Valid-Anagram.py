class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g={}

        for i in s:
            if i not in g:
                g[i]=0
            g[i]+=1
        for i in t:
            if i in g:
                g[i]-=1
        
        if all(value == 0 for value in g.values()):
            return True
        return False