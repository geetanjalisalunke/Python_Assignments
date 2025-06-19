import sys,os,hashlib,time

def CalculateChecksum(path,Blocksize=1024):
    
    fobj=open(path,"rb")    
    hobj=hashlib.md5()
            
    buffer=fobj.read(Blocksize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(Blocksize)  
             
    return hobj.hexdigest()
            
def FindDuplicate(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if (flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if (flag == False):
        print("The path is invalid.")
        exit()

    flag = os.path.isdir(DirectoryName)

    if (flag == False):
        print("Path is valid but target is nnot a Directory.")
        exit()

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):

        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]
    
    return Duplicate  
   
def DisplayResult(mydict):
    result=list(filter(lambda x:len(x)>1,mydict.values()))
    cnt=0
    timestamp=time.ctime()
    filename="Log_%s.txt" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")    
            
    fobj=open(filename,'a')
    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("This is a Log File of Marvellous Automation Script."+"\n")
    fobj.write("This is a Finding Duplicate files in Directory "+"\n")
    fobj.write(Border+"\n")
    
    for value in result:
        
        for subvalue in value:
            fobj.write(subvalue+"\n")
            cnt=cnt+1
            print(subvalue)
            print()
        
        print("Value of count is ",cnt)
            
        cnt=0   
        
    fobj.write("\n"+Border+"\n")
    fobj.write("This file is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")           

def DeleteDuplicate(path)    :
    
    mydict=FindDuplicate(path)
    result=list(filter(lambda x:len(x)>1,mydict.values()))
    cnt=0
    cnt1=0
    for value in result:
        for subvalue in value:
            cnt=cnt+1
            if cnt>1:
                print("Deleted files :",subvalue)
                os.remove(subvalue)
                cnt1=cnt1+1
        cnt=0
    
    print("Total Deleted files is :",cnt1)        
    
    
def main():
    Border = "-"*67
    print(Border)
    print("-----------------------Marvellous Automation-----------------------")
    print(Border)

    if (len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform Directory Cleaning.")
            print("This is the Directory Automation script")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path.")
        
        else:
            
            
            mydict=FindDuplicate(sys.argv[1])
            DisplayResult(mydict)
            DeleteDuplicate(sys.argv[1])
            
    
    else:
        print("Invalid number of command line arguments.")
        print("Use the given flags as : ")
        print("--h : used to display the HELP.")
        print("--u : Used to display the USAGE.")

    print(Border)
    print("-------------------Thank you for using our script------------------")
    print("-----------------------Marvellous Infosystems----------------------")
    print(Border)

if __name__=="__main__":
    main()