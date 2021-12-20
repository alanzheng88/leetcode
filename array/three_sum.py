'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


def calculate_three_sum(nums):
    if len(nums) < 3:
        return []

    duplicate_check = []
    results = []

    for k in range(2, len(nums)):
        for j in range(1, k):
            for i in range(0, j):
                r_i = nums[i]
                r_j = nums[j]
                r_k = nums[k]

                if r_i + r_j + r_k == 0 and {r_i, r_j, r_k} not in duplicate_check:
                    entry = {r_i, r_j, r_k}
                    duplicate_check.append(entry)
                    results.append([r_i, r_j, r_k])

    print(f"duplicate_check: {duplicate_check}")
    print(f"results: {results}")
    return results


def calculate_three_sum2(nums):
    if len(nums) < 3:
        return []

    nums.sort()

    n, results = len(nums), []

    for i in range(n):
        target = nums[i] * -1
        j, k = i + 1, n - 1

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while j < k:
            if nums[j] + nums[k] == target:
                results.append([nums[i], nums[j], nums[k]])
                j += 1
                while 0 < j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif nums[j] + nums[k] < target:
                j += 1
            else:
                k -= 1

    return results
