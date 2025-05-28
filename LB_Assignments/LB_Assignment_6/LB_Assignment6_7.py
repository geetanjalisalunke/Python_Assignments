def Pattern(no1,no2):
    
    for i in range(no1,no2+1):
        print(i,end=" ")
        
def main():
    
    print("Enter First Number")
    value1=int(input())
    print("Enter Second Number")
    value2=int(input())
    
    Pattern(value1,value2)
    
    
if __name__=="__main__":
    main()