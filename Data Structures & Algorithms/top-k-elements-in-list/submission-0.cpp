class Solution 

{
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        ///Im gonna make a vector of pair of in
        int i = 0;
        vector<int*> dictionary;
        vector<int> solution;

        while (i < nums.size())
        {
            lookup_value(nums[i], dictionary);
            
            i++;
        }
        sort_dictionary(dictionary);
        //add to solution
        i = 0;
        while (i < k)
        {
            solution.push_back(dictionary[i][0]);
            std::cout << "just added to solution " << dictionary[i][0] << std::endl;
            i++;
        }
        for (int* entry : dictionary) 
        {
            delete[] entry;
        }
        
        return solution; // leaving this as is so it compiles
    }
private:
    void    lookup_value(int current_value, vector<int*> &dictionary)
    {
        for (int i = 0; i < dictionary.size(); i++)
        {
            if (dictionary[i][0] == current_value)
            {
                dictionary[i][1] += 1;
                std::cout << "just added occurence " << current_value << std::endl;
                return ;
            }
        }

        int *to_add = new int[2];
        to_add[0] = current_value;
        to_add[1] = 0;
        std::cout << "just added to my dic " << current_value << std::endl;
        dictionary.push_back(to_add);
    }
    static bool compare_counts(int* a, int* b) 
    {
        return (a[1] > b[1]);
    }
    void sort_dictionary(std::vector<int*>& dictionary) 
    {
        std::sort(dictionary.begin(), dictionary.end(), compare_counts);
    }
};
