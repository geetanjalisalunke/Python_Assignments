import multiprocessing 
import threading
import time

def sum() :
    add=0
    for i in range(10000001):
        add=add+i

def sum1(no1,no2) :
    return no1+no2

def main():
    start_time=time.time()
    sum()
    end_time=time.time()
    print("Execution time for normal function",end_time-start_time)
    
    start_time=time.time()
    T1=threading.Thread(target=sum)
    T1.start()
    T1.join()
    end_time=time.time()
    print("Execution time for Thread",end_time-start_time)
    
    start_time=time.time()
    p1=multiprocessing.Process(target=sum)
    p1.start()
    p1.join()
    end_time=time.time()
    print("Execution time for Process",end_time-start_time)
    
    
if __name__=="__main__":
    main()