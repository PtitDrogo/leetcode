#include <limits.h>

class Solution 
{
public:
    int longestConsecutive(vector<int>& nums) 
    {
        int prev_num = INT_MAX;
        int longest_sequence = 0;
        int current_sequence = 0;

        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] - 1 == prev_num)
                current_sequence++;
            else if (nums[i] != prev_num)
            {
                if (current_sequence > longest_sequence)
                    longest_sequence = current_sequence;
                current_sequence = 1;
            }
            prev_num = nums[i];
        }
        if (current_sequence > longest_sequence)
            longest_sequence = current_sequence;
        return (longest_sequence);
    }
};
