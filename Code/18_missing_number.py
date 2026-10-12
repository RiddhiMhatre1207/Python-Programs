def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [1, 2, 4, 5]
n = 5

result = find_missing_number(nums, n)
print("Missing number:", result)
