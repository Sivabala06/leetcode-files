class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g={}
        f={}
        for i in s:
            if i not in g:
                g[i]=0
            g[i]+=1
        for i in t:
            if i not in f:
                f[i]=0
            f[i]+=1
        if f==g:
            return True
        return False