def Chk_char(ch):
    lst=['a','e','i','o','u','A','E','I','O','U']
    if ch in lst:
        print(f"'{ch}' is Vowel")
    else:
        print(f"'{ch}' is Consonant")

def main():
    
    print("Enter the Character")
    ch=input()
    Chk_char(ch)
    
if __name__=="__main__":
    main()