def ParkingClaculate(no):
    
    if no<=3:
        return 30*no
    else :
        return no*5
        
def main():
    
    print("Enter Number")
    value1=float(input())
    
    
    ret=ParkingClaculate(value1)
    print("Total Amount",ret)
    
if __name__=="__main__":
    main()