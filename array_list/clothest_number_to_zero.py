"""Given an integer array nums of size n, return the number with the closest to 0 in nums. If there is a multiple answers, return the number with the largest 
value.aExample 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105"""


# Variant 1
def closest_to_zero(nums: list) -> int:
    closest = nums[0]
    for n in nums:
        if abs(n) < abs(closest):
            closest = n
    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


print(closest_to_zero([2, -1, 1]))
print(closest_to_zero([-4, -2, 4, 8]))
