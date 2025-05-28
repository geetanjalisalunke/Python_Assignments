def DisplayNo(no):
    a=[]
    while(no>0):
        
        val=no%10
        
        match val:
            
            case 0:
                a.append("Zero")
            case 1:
                a.append("One")
            case 2:
                a.append("Two")
            case 3:
                a.append("Three")
            case 4:
                a.append("Four")
            case 5:
                a.append("Five")
            case 6:
                a.append("Six")
            case 7:
                a.append("Seven")
            case 8:
                a.append("Eight")
            case 9:
                a.append("Nine")
                
        no=no//10
    
    a.reverse()
    return a
    
def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret=DisplayNo(value1)
    print(ret)
    
    for val in ret:
        print(val,end=" ")
    
if __name__=="__main__":
    main()