import multiprocessing
def square(no):
    print(no*no)
    

def main():
    a=[100000000,20000000,30000000,40000000,50000000]
    
    for i in a:
        process1=multiprocessing.Process(target=square,args=(i,))
        process1.start()
        process1.join()
        process1.terminate()
        print("Process Terminate")
        
if __name__=="__main__":
    main()