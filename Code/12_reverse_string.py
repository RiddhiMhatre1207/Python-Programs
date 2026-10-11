def reverse_string(s):
    rev = ""
    for i in range(len(s)):
        rev = s[i] + rev
    return rev

s = input("Enter a string: ")
print("Reversed string:", reverse_string(s))