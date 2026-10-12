def find_element(nums, target):
    if target in nums:
        return True
    return False


# Example
nums = [10, 20, 30, 40, 50]
target = 30

print(find_element(nums, target))
