cnt=0
def Count_Zero(no):
    
    if no==0:
        return
    val=no%10
    if val==0:
        global cnt
        cnt=cnt+1
    Count_Zero(no//10)
    
    return cnt
  
        
def main():
    
    print("Enter Number")
    value1=int(input())
    ret=Count_Zero(value1)
    print(ret)
    
    
    
if __name__=="__main__":
    main()