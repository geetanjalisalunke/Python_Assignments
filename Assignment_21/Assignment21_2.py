import psutil,sys

def ProcessDisplay(Process_name):
    
    Border="*" * 80
    print(Border)
    print("Information of currently running processess :")
    print(Border)
    
    for proc in psutil.process_iter():
        try: 
            info=proc.as_dict(attrs=['pid','name','username'])
            if info['name']==Process_name:
                print(info)
        except Exception:
            print("Exception Occured")
   

def main():
    p_name=sys.argv[1]
    ProcessDisplay(p_name)

if __name__=="__main__":
    main()