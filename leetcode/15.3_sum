class Solution {
public:
//2-Pointer
    vector<vector<int>> threeSum(vector<int>& nums) {
       vector<vector<int>>ans;
       int n=nums.size();int j,k,sum;
       sort(nums.begin(),nums.end());
       for(int i=0;i<n;i++){
       if(i>0 && nums[i]==nums[i-1]){
        continue;
       }
       j=i+1;
       k=n-1;
       while(j<k){
        sum=nums[i]+nums[j]+nums[k];
        if(sum<0) j++;
        else if(sum>0) k--;
        else{
            ans.push_back({nums[i],nums[j],nums[k]});
            j++;
            k--;
        
        while(j<k && nums[j]==nums[j-1]){
            j++;
        }
        }
       }
       }
return ans;
    }
};