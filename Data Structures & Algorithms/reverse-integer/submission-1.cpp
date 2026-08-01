#include <limits>
#include <cmath>

class Solution 
{
    public:
        int reverse(int x) 
        {
            long digits_num = num_len(x);
            long tmp;
            double result = 0;

            if (digits_num == 1)
                return (x);
            while (digits_num != 0)
            {
                tmp = x % 10 * pow(10, digits_num - 1);
                result = myAdd(result, tmp);
                x /= 10;
                digits_num--;
            }

            if (result < std::numeric_limits<int>::lowest() || result > std::numeric_limits<int>::max())
                return (0);
            return (result); //Not casting because I trust my compiler <3

        }
        long myAdd(long a, long b)
        {
            //slighty magic adding function but in a nutshell its just
            // carrying to the everytime theres a 1 in both a and b
            // just like if you went above 10 in a regular addition of two digits
            long carry = a & b;
            long result = a ^ b;
            while(carry != 0)
            {
                long shiftedcarry = carry << 1;
                carry = result & shiftedcarry;
                result ^= shiftedcarry;
            }
            return result;
        }
        int num_len(int x)
        {
             int result = 0;

            do
            {
                x /= 10;
                result++;
            } while (x != 0);
            return result;
        }
};
