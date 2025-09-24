class Solution {
public:
    int search(vector<int>& nums, int target) {
        int st=0;
        int end=nums.size()-1;
        int mid;
        while(st<=end){
            mid=st+((end-st))/2; 
            if(nums[mid]==target)
            return mid;  
            if(nums[st]<=nums[mid]){  //LEFT SORTED
                if(nums[st]<=target && target<=nums[mid]){
                    end=mid-1;
                }
                else
                st=mid+1;
            }
            else { //RIGHT SORTED
                if(nums[mid]<=target && target<=nums[end]){
                st=mid+1;
            }
            else
            end=mid-1;
         
            }
          }
          return -1;
    }
};