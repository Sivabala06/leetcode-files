class Solution {
public:
    void backtrack(int start,vector<int>&curr,vector<vector<int>>&res,vector<int>&canditates,int target){
    if (target<0) return;
if (target==0){
    res.push_back(curr);
    return;
}
for(int i=start;i<canditates.size();i++){
    if(i>start &&canditates[i-1]==canditates[i])
    continue;
    curr.push_back(canditates[i]);
    backtrack(i+1,curr,res,canditates,target-canditates[i]);
    curr.pop_back();
}
}
    vector<vector<int>> combinationSum2(vector<int>& canditates, int target) {
        vector<vector<int>>res;
        vector<int>curr;
        sort(canditates.begin(),canditates.end());
        backtrack(0,curr,res,canditates,target);
        return res;
    }
};