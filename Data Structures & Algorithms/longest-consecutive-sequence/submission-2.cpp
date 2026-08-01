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
            {
                current_sequence++;
                // std::cout << "current sequence " << current_sequence << std::endl;
                // std::cout << "new prev num and current nums[i] : " << prev_num << ", " << nums[i] << std::endl;
            }
            else if (nums[i] == prev_num)
            {
                continue;
            }
            else
            {
                if (current_sequence > longest_sequence)
                    longest_sequence = current_sequence;
                current_sequence = 1;
                // std::cout << "new prev num and current nums[i] : " << prev_num << ", " << nums[i] << std::endl;
            }
            prev_num = nums[i];
        }
        if (current_sequence > longest_sequence)
            longest_sequence = current_sequence;
        return (longest_sequence);
    }
};

//I go trough my array ONCE
// Current number = MAX INT
// 
// is it smaller than my current ?
// if yes, current sequence = 0 and longest sequence = current_sequence
// if no, is it exactly +1 my current number ?
// if yes, current sequence ++, go next number
//if no, do nothing go next
// if 
// 1 2 3 4 5 -1 - 10 - 9-8 -7 -6 -5 -4 -3 -2 -1 
