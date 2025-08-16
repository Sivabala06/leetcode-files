class Solution {
public:
void backtrack(vector<int>&curr,vector<vector<int>>&res,vector<int>&nums){
    if(nums.size()==curr.size()){
        res.push_back(curr);
        return;
    }
    for(int i=0;i<nums.size();i++){
        if(find(curr.begin( ), curr.end(), nums[i]) == curr.end())
        {
            curr.push_back(nums[i]);
            backtrack(curr,res,nums);
            curr.pop_back();
        }
    }
}
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>res;
        vector<int>curr;
        backtrack(curr,res,nums);
        return res;
    }
};