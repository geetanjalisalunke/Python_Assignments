
def print_number(no):
    
    if no==0:
        return
    print_number(no-1)
    print(no)
    
    
        
def main():
    
    print("Enter Number")
    value1=int(input())
    print_number(value1)
    
    
    
if __name__=="__main__":
    main()