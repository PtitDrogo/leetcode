class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const copy = nums.concat(nums)
        return copy
    }
}
