numbers = list(map(int, input("Enter numbers: ").split()))

result = second_largest(numbers)

if result is not None:
    print("Second largest number:", result)
else:
    print("There is no second largest distinct number.")

