class Solution {
public:

    std::map<char, int> map;
    bool isAnagram(std::string s, std::string t) 
    {
        //Filling an hashmap with the letters because leetcode says hasmap good
        for (int i = 0; i < s.size(); i++)
        {
            if (map.find(s[i]) == map.end())
            {
                map[s[i]] = 1;
            }
            else
            {
                map[s[i]] += 1;
            }
        }
        
        for (int i = 0; i < t.size(); i++)
        {
            if (map.find(t[i]) == map.end())
            {
                return false;
            }
            else
            {
                if (map[t[i]] > 0)
                    map[t[i]] -= 1;
                else
                {
                    return (false);
                }
            }
        }
        //Checking if every element in my hash table is present 0 time
        for (std::map<char, int>::const_iterator it = map.begin(); it != map.end(); it++)
        {
            if (it->second != 0)
                return false;
        }
        return (true);
    }
};