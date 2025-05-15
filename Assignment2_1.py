import Arithmetic as ar

def main():
    
    print("Enter the First number")
    val1=int(input())
    print("Enter the Second number")
    val2=int(input())
    result=ar.Add(val1,val2)
    print("Addition is : ",result)
    result=ar.Sub(val1,val2)
    print("Substraction is : ",result)
    result=ar.Mult(val1,val2)
    print("Multiplication is : ",result)
    result=ar.Div(val1,val2)
    print("Division is : ",result)
    
if __name__=="__main__":
    main()
