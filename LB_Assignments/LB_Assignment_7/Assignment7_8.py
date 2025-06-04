def Display(no):
    if no>='a' and no<='z':
        print("It is a Small Letter")
    if no>='A' and no<='Z':
        print("It is a Capital Letter")
    if no>='0' and no<='9':
        print("It is a Digit")
    
def main():
    
    print("Enter Character")
    value1=input()
    
    Display(value1)
    


if __name__=="__main__":
    main()