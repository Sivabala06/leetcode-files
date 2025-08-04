class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
    int ns=nums.size();
    unordered_map<int,int>m;
    for(int i=0;i<ns;i++){
            if(m.count(nums[i])){ 
                if(abs(i-m[nums[i]])<=k) return true;
            }
   m[nums[i]]=i;
    }
    return false;  
    }
};