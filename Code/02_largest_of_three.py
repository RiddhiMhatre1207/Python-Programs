def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == " __main__ ":
    print(find_largest(2,7,9))
    print(find_largest(11,-15,-9))