class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        c=0
        r=[]
        pairs={
            ')':'('
        }

        for i in s:
            if i in '(':
                r.append(i)
            
            else:
                if not r:
                    c-=1
                    return False
                if r[-1] != pairs[i]:
                    c-=1
                    return False
                
                r.pop()
                c+=1
        return c