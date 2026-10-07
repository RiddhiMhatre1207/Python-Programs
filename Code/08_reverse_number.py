def reverse_number(num):
    sign = -1 if num < 0 else 1
    num = abs(num)

    reverse = 0

    while num >0:
        digit = num % 10
        reverse = reverse*10+digit
        num = num//10

    return sign * reverse 
    if __name__ == "__main__":
        print(reverse_number(1234567))