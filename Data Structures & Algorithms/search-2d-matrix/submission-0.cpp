class Solution {
private:
    int left;
    int right;
    int middle;


public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) 
    {
        if (matrix.empty() || matrix[0].empty())
            return false;
        
        int cols = matrix[0].size();
        int row = matrix.size();
        int middle_value;
        left = 0;
        right = (row * cols) - 1;

        while (left <= right)
        {
            middle = left + (right - left) / 2;
            middle_value = matrix[middle / cols][middle % cols];
            if (middle_value == target)
                return (true);
            if (middle_value < target)
            {
                left = middle + 1;
            }
            else if (middle_value > target)
            {
                right = middle - 1;
            }
        }
        return (false);
    }
};
