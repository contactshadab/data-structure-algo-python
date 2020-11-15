'''
https://leetcode.com/problems/product-of-array-except-self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''


# Intuition: Product of left * product of right = product of array except self
# To save space we'll use result to store product of left and will generate product of right on the fly
# Run time complexity: O(n)
# Space complexity: O(1), if not cpounting space needed for result
def product_except_self(nums):
    result = [0 for i in range(len(nums))]
    result[0] = 1
    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1]
    product_right = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] = result[i] * product_right
        product_right = product_right * nums[i]

    return result


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))
