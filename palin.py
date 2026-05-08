def Palindrome(text):
    
    s = text.replace(" ","").lower()
    return s == s[::-1]

string1 = str(input("Enter a string: "))
string2 = str(input("Enter a string2: "))
print(Palindrome(string1))
print(Palindrome(string2))
