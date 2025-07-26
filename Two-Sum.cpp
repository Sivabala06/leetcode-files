class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int ns= nums.size();
        vector <int>res;
        unordered_map<int,int>m;
        for(int i=0;i<ns;i++){
          int b=target-nums[i];
          if(m.count(b)){
            res.push_back(m[b]);
            res.push_back(i);
            return res;
          }
        else m[nums[i]]=i;
        }
        return res;
}};