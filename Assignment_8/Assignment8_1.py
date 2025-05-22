import threading 

def display_even():
    
    for i in range(11):
        if i%2==0:
            print("Thread even",i)
  
def display_odd():
    
    for i in range(11):
        if i%2!=0:
            print("Thread odd",i)      

def main():
    
    even=threading.Thread(target=display_even)
    odd=threading.Thread(target=display_odd)
    
    even.start()
    odd.start()
    
    even.join()
    odd.join()

if __name__=="__main__":
    main()