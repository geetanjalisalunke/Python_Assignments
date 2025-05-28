def ChkPythagorus(no1,no2,no3):
    
    if no3**2==(no1**2) + (no2**2):
        return True
    else:
        return False
    

def main():
    
    print("Enter First Side")
    value1=float(input())
    print("Enter First Side")
    value2=float(input())
    print("Enter First Side")
    value3=float(input())
    
    ret=ChkPythagorus(value1,value2,value3)
    if ret==True:
        print("it is Pythagorean triple")
    else:
        print("it is not Pythagorean triple")
    
if __name__=="__main__":
    main()