import threading

def display():
    for i in range(1,51):
        print("Thread 1",i)

def display_rev():
    for i in range(50,0,-1):
        print("Thread 2",i)
        
def main():
    Thread1=threading.Thread(target=display)
    Thread2=threading.Thread(target=display_rev)
    
    Thread1.start()
    Thread1.join()
    Thread2.start()
    Thread2.join()

if __name__=="__main__":
    
    main()