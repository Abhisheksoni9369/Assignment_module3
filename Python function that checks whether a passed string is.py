def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

string1 = "radar"
string2 = "Hello World"

if is_palindrome(string1):
    print(f"{string1} is a palindrome")
else:
    print(f"{string1} is not a palindrome")

if is_palindrome(string2):
    print(f"{string2} is a palindrome")
else:
    print(f"{string2} is not a palindrome")
