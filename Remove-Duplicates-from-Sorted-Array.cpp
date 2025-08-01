class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       int res=1;
       int ns=nums.size();
       for(int i=1;i<ns;i++){
        if(nums[i]!=nums[i-1]){
            nums[res]=nums[i];
            res++;
        }
       }
        return res;
    }
};