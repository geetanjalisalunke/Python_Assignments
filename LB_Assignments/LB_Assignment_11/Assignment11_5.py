def Percentage(lst):
    
    for num in lst:
        if num<35:
            print("Fail")
        elif num>=35 and num<=50:
            print("Pass Class")
        elif num>50 and num<=60:
            print("Second Class")
        elif num>61 and num<=70:
            print("First Class")
        elif num>70:
            print("First Class with Distinction")
    
    
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(float(input()))
    
    Percentage(a)
    

    
    
if __name__=="__main__":
    main()