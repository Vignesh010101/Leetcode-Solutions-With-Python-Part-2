class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        int n=target.size();
        vector<int>diff(n);
        long long int opr=0;
        int prev=0;
        for(int i=0;i<n;i++)
        {
            diff[i]=target[i]-nums[i];
            int curr=diff[i];
            if((prev>0&&curr<0)||(prev<0&&curr>0))
            {
                opr+=abs(diff[i]);
            }
            else if(abs(curr)>abs(prev))
            {
                opr+=abs(curr-prev);
            }
            prev=diff[i];
        }
        return opr;
    }
};