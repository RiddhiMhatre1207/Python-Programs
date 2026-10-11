def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


# Take input from user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = remove_duplicates(numbers)

print("List after removing duplicates:", result)
