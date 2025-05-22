import threading


def chk_small(value):
    print("Id of small thread",threading.get_ident())
    print("Name of thread is",threading.current_thread().name)
    cnt=0
    for i in value:
        if i>='a' and i<='z':
           cnt=cnt+1
    print("Count of small letter in string is :",cnt)
    
def chk_capital(value):
    print("Id of Capital thread",threading.get_ident())
    print("Name of thread is",threading.current_thread().name)
    cnt=0
    for i in value:
        if i>='A' and i<='Z':
           cnt=cnt+1
    print("Count of capita letter in string is :",cnt)
    
def chk_digit(value):
    print("Id of digit thread",threading.get_ident())
    print("Name of thread is",threading.current_thread().name)
    cnt=0
    for i in value:
        if i.isdigit():
           cnt=cnt+1
    print("Count of digit in string is :",cnt)
    
def main():
  
  print("Enter the String")  
  name=input()
  
  
  small=threading.Thread(target=chk_small,args=(name,))
  capital=threading.Thread(target=chk_capital,args=(name,))
  digit=threading.Thread(target=chk_digit,args=(name,))
  
  small.start()
  capital.start()
  digit.start()
  
  small.join()
  capital.join()
  digit.join()
  
print("Id of main thread",threading.get_ident())
print("Name of thread is",threading.current_thread().name)
if __name__=="__main__":
    main()