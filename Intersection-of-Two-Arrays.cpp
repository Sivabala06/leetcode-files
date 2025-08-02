class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int ns1=nums1.size(),ns2=nums2.size();
        vector<int>res;
        if(ns1>ns2){
            for(int i=0;i<ns2;i++){
                for(int j=0;j<ns1;j++){
                    if(nums2[i]==nums1[j]) res.push_back(nums2[i]);
                }
            }
        }
        else{ for(int i=0;i<ns1;i++){
                for(int j=0;j<ns2;j++){
                    if(nums1[i]==nums2[j]) res.push_back(nums1[i]);
                }
            }
        }
        set<int>uniqueSet(res.begin(), res.end());  // Automatically removes duplicates
    return vector<int>(uniqueSet.begin(), uniqueSet.end());
        
    }
};