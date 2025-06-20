import psutil,sys,os,time,json

def ProcessDisplay(Dir_name):
    
    flag=os.path.isabs(Dir_name)
    
    if flag==False:
        flag=os.path.abspath(Dir_name)
        
    flag=os.path.exists(Dir_name)
    
    if flag==False:
        os.mkdir(Dir_name)
    else:
        print("Directory is already exists")    
        exit()
        
    flag=os.path.isdir(Dir_name)
    
    if flag==False:
        print("Path is valid but target is not a Directory.")
        exit()
        
    Border = "-"*80

    path=os.path.join(Dir_name,'Log.txt')
    fobj=open(path,'x')
    
    timestamp=time.ctime()    
    fobj.write(Border+"\n")
    fobj.write("This is a Log File of Marvellous Automation Script."+"\n")
    fobj.write("This is a Finding running processes "+"\n")
    fobj.write(Border+"\n")
        
    for proc in psutil.process_iter():
        try: 
            info=proc.as_dict(attrs=['pid','name','username'])
            fobj.write(json.dumps(info)+"\n")
        except Exception:
            print("Exception Occured")
   
    fobj.write("\n"+Border+"\n")
    fobj.write("This file is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n") 
    
def main():
    Dir_name=sys.argv[1]
    ProcessDisplay(Dir_name)

if __name__=="__main__":
    main()