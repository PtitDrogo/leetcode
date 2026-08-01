class Solution {
public:
    int findMin(std::vector<int> &nums) 
    {
        int left = 0;
        int right = nums.size() - 1;
        int min_val = nums[left];
        int middle = (left + right) / 2;

        // if (right == 0)
        //     return nums[0];
        while (left <= right)
        {
            if (min_val <= nums[middle])
            {
                left = middle + 1;
            }
            else if (min_val > nums[middle])
            {
                right = middle - 1;
                min_val = nums[middle];
            }
            middle = (left + right) / 2;
        }
        return min_val;
    }
};
