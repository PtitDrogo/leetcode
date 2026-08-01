class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //I have a set, if I add to it, it removes dupplicate.
        //So if my set has a length not equal to nums, it has a dupplicate.

        std::unordered_set<int> seen;
        for (int num : nums) {
            seen.insert(num);
        }
        return nums.size() != seen.size();
    }
};