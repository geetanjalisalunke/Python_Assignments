def Add(a,b):
    return a+b
def Sub(a,b):
    return a-b
def Mult(a,b):
    return a*b
def Div(a,b):
    return a/b

def main():
    
    print("Enter the First Number")
    no1=int(input())
    print("Enter the Second Number")
    no2=int(input())
    
    ret=Add(no1,no2)
    print("Sum :",ret)
    ret=Sub(no1,no2)
    print("Difference :",ret)
    ret=Mult(no1,no2)
    print("Product :",ret)
    ret=Div(no1,no2)
    print("Division :",ret)
    

if __name__=="__main__":
    main()