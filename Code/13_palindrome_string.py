def is_palindrome(s):
    rev = ""
    for i in range(len(s)):
        rev = s[i] + rev

    if s == rev:
        return True
    else:
        return False

s = input("Enter a string: ")

if is_palindrome(s):
    print("Palindrome String")
else:
    print("Not a Palindrome String")