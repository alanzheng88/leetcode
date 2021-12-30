'''
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''
from typing import List


def three_sum(nums: List[int], target: int) -> List[List[int]]:
    n, result = len(nums), []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j, k = i + 1, n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == target:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                while i < j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif total < target:
                j += 1
            else:
                k -= 1
    return result


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()

    n, result = len(nums), []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        r_i = nums[i]
        new_target = target - r_i
        new_list = list(nums)
        del new_list[i]
        new_list = list(new_list[i:])
        three_sum_result = three_sum(new_list, new_target)

        if not three_sum_result:
            continue
        else:
            print(three_sum_result)
            for res in three_sum_result:
                r_j, r_k, r_l = res[0], res[1], res[2]
                arr = [r_i, r_j, r_k, r_l]
                result.append(arr)

    return result
