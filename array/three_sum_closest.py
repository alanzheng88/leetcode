"""
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Input: nums = [0,0,0], target = 1
Output: 0

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
from typing import List


def calculate_three_sum_closest(nums: List[int], target: int) -> int:
    n, smallest_target_diff, closest_sum = len(nums), 9999999, 9999999

    if n < 3:
        raise Exception('nums must have at least 3 numbers')

    nums.sort()

    for i in range(n):
        left_index = i + 1
        right_index = n - 1

        while left_index < right_index:
            sum_total = nums[i] + nums[left_index] + nums[right_index]
            target_diff = abs(target - sum_total)

            if target_diff < smallest_target_diff:
                smallest_target_diff = target_diff
                closest_sum = nums[i] + nums[left_index] + nums[right_index]

            if sum_total == target:
                return closest_sum
            elif sum_total <= target:
                left_index += 1
            else:
                right_index -= 1

    return closest_sum
