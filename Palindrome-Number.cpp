class Solution {
public:
    bool isPalindrome(int n) {
       if(n<0) return false;
        long int r=0;
        int temp=n;
        while(n>0)
        {
            r=(r*10)+(n%10);
            n=n/10;
        }
        return (temp==r); 
    }
};