class Solution {
public:
    int maxArea(vector<int>& n) {
        int st=0;
        int end=n.size()-1;
        int ans=0;
        while(st<end){
            int width= end-st;
           int  height=min(n[st],n[end]);
           int area=width*height;
           ans=max(area,ans);
           if(n[st]<n[end])
           st++;
           else
           end--;
                  }
                  return ans;
    }
    
};