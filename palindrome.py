def palindrome (str):
    str1=str.lower().replace(" ","")
    
    rev_str=""
    
    for char in str1:
        rev_str=char+rev_str
    
    if rev_str==str1: #if s == s[::-1]:
        print("Given string is Palindrome")
    else:
        print("Given string is not a Palindrome")
    


print("Enter the String")
str1=input()
palindrome(str1)