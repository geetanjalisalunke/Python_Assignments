def CalculateMin(no):
    
    return no*60
        
def main():
    
    print("Enter Number")
    value1=int(input())
    
    
    ret=CalculateMin(value1)
    print("Total Minute",ret)
    
if __name__=="__main__":
    main()