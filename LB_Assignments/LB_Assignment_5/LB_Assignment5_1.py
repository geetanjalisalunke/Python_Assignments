def MinDigit(no):
    
    val=no%10
    min=val
    while(no>0):
        
        val=no%10
        if val<min:
            min=val
        no=no//10
    return min


def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret=MinDigit(value1)
    print("Minimum digit:",ret)
    
if __name__=="__main__":
    main()