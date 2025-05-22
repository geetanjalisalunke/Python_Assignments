import multiprocessing 


def factorial(no):
    res=1
    for i in range(1,no+1):
        res=res*i
    return res  
    

def main():
    a=[10,20,30,40,50]
    
    process1=multiprocessing.Pool()
    result=process1.map(factorial,a)
    print(result)
        
if __name__=="__main__":
    main()