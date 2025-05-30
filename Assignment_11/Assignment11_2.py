fact=1
def factorial(no):
    
    if no==0:
        return
    global fact
    fact=fact*no
    factorial(no-1)
    return fact
        
def main():
    
    print("Enter Number")
    value1=int(input())
    ret=factorial(value1)
    print(ret)
    
    
    
if __name__=="__main__":
    main()