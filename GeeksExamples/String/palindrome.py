# Python Program to check if a string is palindrome or not

def ispalindrome(s):
    if s==s[::-1]:
        print(f"Yes {s} is a palindrome.")
    else:
        print(f"No {s} is not palindrome.")

st = "malayalam"
ispalindrome(st)
