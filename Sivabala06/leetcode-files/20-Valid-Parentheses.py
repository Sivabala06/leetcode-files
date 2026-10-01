class Solution:
    def isValid(self, s: str) -> bool:
        r=[]
        for i in s:
            if (i=='(' or i=='[' or i=='{'):
                r.append(i)
            else:
                if not r:
                    return False
                if i==')':
                    if r[-1]=='(':
                        r.pop()
                    else:
                        return False
                if i==']':
                    if r[-1]=='[':
                        r.pop()
                    else:
                        return False
                if i=='}':
                    if r[-1]=='{':
                        r.pop()
                    else:
                        return False
        if not r :
            return True
        return False

                
        
        