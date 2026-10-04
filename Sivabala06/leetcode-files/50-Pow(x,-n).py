class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return float(x**n)
        if n==0:
            return 1
        
        def po(n):
            if n==1:
                return x
            print(x*n)
            return x*po(n-1)
        if n<0:
            res=po(-n)
            return 1/res
        res=po(n)
        return res