#include <limits>
#include <cmath>

class Solution 
{
    public:
        int reverse(int x) 
        {
            long digits_num = num_len(x);
            long tmp;
            bool did_overflow = false;
            double result = 0;

            if (digits_num == 1)
                return (x);
            while (digits_num != 0)
            {
                tmp = x % 10 * pow(10, digits_num - 1);
                result = myAdd(result, tmp, did_overflow);
                if (did_overflow == true)
                    return (0);
                x /= 10;
                digits_num--;
            }

            if (result < std::numeric_limits<int>::lowest() || result > std::numeric_limits<int>::max())
                return (0);
            return (result);

        }
        long myAdd(long a, long b, bool &did_overflow)
        {
            //slighty magic adding function but in a nutshell its just
            // carrying to the everytime theres a 1 in both a and b
            // just like if you went above 10 in a regular addition of two digits
            long carry = a & b;
            long result = a ^ b;
            long overflow_check;

            overflow_check = result;
            while(carry != 0)
            {
                long shiftedcarry = carry << 1;
                carry = result & shiftedcarry;
                result ^= shiftedcarry;
            }
            if (a > 0)
            {
                if (overflow_check > result)
                {
                    did_overflow = true;
                    return (0);
                }
            }
            else if (a > 0)
            {
                if (overflow_check < result)
                {
                    did_overflow = true;
                    return (0);
                }
            }
            return result;
        }
        //manual checking of shame
        bool is_result_outside_of_int_range(double x)
        {
            if (num_len(x) != 10)
                return false;
            
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
