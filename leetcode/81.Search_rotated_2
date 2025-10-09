class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int st=0;
        int end=nums.size()-1;
        while(st<=end){
            int mid=st+(end-st)/2;
            if(nums[mid]==target)
            return true;
             if (nums[st] == nums[mid] && nums[mid] == nums[end]) {
                st++;
                end--;
            }
            else if(nums[st]<=nums[mid]){  //LEFT SORTED
               if(nums[st]<=target && target<=nums[mid]){
                end=mid-1;
                // return true;
               }
               else
               st=mid+1;
            //    return true;
        }
            else{
            if(nums[mid]<=target && target<=nums[end]){
st=mid+1;
// return true;
            }
            else{
                end=mid-1;
                // return false;
            }
        }
        }return false;
    }
};