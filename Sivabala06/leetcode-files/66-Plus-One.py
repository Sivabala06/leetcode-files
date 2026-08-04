class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=digits[-1]+1
        sum=0
        
        if l>9 and len(digits)>1:
            j=len(digits)
            for i in digits:
                sum=sum+(i*(10**(j-1)))
                j-=1
            t=sum+1
            git=[int(i) for i in str(t)]
            return git
        if l>9:
            digits.pop()
            digits=[int(i) for i in str(l)]
            return digits
        digits.pop()
        digits.append(l)
        return digits

        
            
        