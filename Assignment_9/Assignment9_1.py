import threading
import time

def display1():
    for i in range (1,6):
        print("Thread 1",i)
        time.sleep(1)
def display2():
    for i in range (1,6):
        print("Thread 2",i)
        time.sleep(1)
def display3():
    for i in range (1,6):
        print("Thread 3",i)
        time.sleep(1)
def main():
    Thread1=threading.Thread(target=display1)
    Thread2=threading.Thread(target=display2)
    Thread3=threading.Thread(target=display3)
    
    Thread1.start()
    Thread2.start()
    Thread3.start()
    Thread1.join()
    Thread2.join()
    Thread3.join()

if __name__=="__main__":
    
    main()