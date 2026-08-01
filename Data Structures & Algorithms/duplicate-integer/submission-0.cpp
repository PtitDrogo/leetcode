class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
        std::unordered_map<int, int> map;
        for (unsigned int i = 0; i < nums.size(); i++)
        {
            if (map.count(nums[i]) == 1)
                return true;
            else
            {
                map[nums[i]] = i;
            }
        }
        return false;
    }
};
