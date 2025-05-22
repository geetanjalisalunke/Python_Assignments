import threading 

def add_evenfact(no):
    sum=0
    for i in range(1,no+1):
        if no%i==0:
            if i%2==0:
                sum=sum+i
    print("Sum of Even factor",sum)
  
def add_oddfact(no):
    sum=0
    for i in range(1,no+1):
        if no%i==0:
            if i%2!=0:
                sum=sum+i
    print("Sum of Odd factor",sum)   

def main():
    
    print("Enter the number")
    no=int(input())
    
    evenfactor=threading.Thread(target=add_evenfact,args=(no,))
    oddfactor=threading.Thread(target=add_oddfact,args=(no,))
    
    
    evenfactor.start()
    oddfactor.start()
    
    evenfactor.join()
    oddfactor.join()
    
    print("Exit from main")

if __name__=="__main__":
    main()