class Solution {
public:
 /*void traverse(string digits ,string mapping[],string curr,vector<string>&res){
    if(digits.empty()) res.push_back(curr);
    else{
        string letter=mapping[digits[0]-'0'];
        for(char choice : letter)
         traverse(digits.substr(1),mapping,curr+choice,res);
    }
 }
    vector<string> letterCombinations(string digits) {
        vector<string>res;
        if(digits.empty()) return {};
        string mapping[]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        traverse(digits,mapping,"",res);
        return res;*/
    vector<string> letterCombinations(string digits) {
        if(digits.empty()) return {};
        string mapping[]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        vector<string>res={""};
        for(char digit :digits){
            vector<string>curr;
            for(string comb:res){
                for(char choice:mapping[digit-'0']){
                    curr.push_back(comb+choice);
                }
            }
            res=curr;
        }
        return res;
        
     }
};