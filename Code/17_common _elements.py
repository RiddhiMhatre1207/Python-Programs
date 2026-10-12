def common_elements(list1, list2):
    return list(set(list1) & set(list2))


# Test code
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = common_elements(list1, list2)

print("Common elements:", result)
