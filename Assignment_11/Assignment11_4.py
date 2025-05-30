res=1
def Power(no1,no2):
    
    if no2==0:
        return
    global res
    res=res*no1
    Power(no1,no2-1)
    return res
  
        
def main():
    
    print("Enter First Number")
    value1=int(input())
    print("Enter Second Number")
    value2=int(input())
    ret=Power(value1,value2)
    print(ret)
    
    
    
if __name__=="__main__":
    main()