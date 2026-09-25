class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sw=[]
        for i in s.lower():
            if i.isalnum():
                sw.append(i)
        qw=''.join(sw)
        
        return qw==qw[::-1]
        