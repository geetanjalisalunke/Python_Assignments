import threading 

def add_evenlist(a):
    sum=0
    for i in a:
        if i%2==0:
            sum=sum+i
    print("Sum of Even Number",sum)
  
def add_oddlist(a):
    sum=0
    for i in a:
        if i%2!=0:
            sum=sum+i
    print("Sum of Odd Number",sum)   

def main():
    
    print("Enter the number")
    no=int(input())
    
    a=[]
    print("Enter the Elements")
    
    for i in range(no):
        a.append(int(input()))

    evenlist=threading.Thread(target=add_evenlist,args=(a,))
    oddlist=threading.Thread(target=add_oddlist,args=(a,))
    
    evenlist.start()
    oddlist.start()
    
    evenlist.join()
    oddlist.join()
    
if __name__=="__main__":
    main()