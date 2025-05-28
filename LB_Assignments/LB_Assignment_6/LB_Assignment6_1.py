def RentCalculate(no):
    
    if no<=120:
        return 15*no
    else :
        return 120*15+((no-120)*10)
        
        
    

def main():
    
    print("Enter Number")
    value1=float(input())
    
    
    ret=RentCalculate(value1)
    print("Rent of car",ret)
    
if __name__=="__main__":
    main()