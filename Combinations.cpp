class Solution {
public:
void backtrack(int start,int k,int n,   vector<int>&curr,vector<vector<int>>&res){
    if(curr.size()==n){
        res.push_back(curr);
        return;
    }
    for(int i= start;i<=k;i++){
        curr.push_back(i);
        backtrack(i+1,k,n,curr,res);
        curr.pop_back();
    }
}
    vector<vector<int>> combine(int k, int n) {
         vector<vector<int>>res;
        vector<int>curr;
        backtrack(1,k,n,curr,res);
        return res;
    }
};