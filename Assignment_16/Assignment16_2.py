import os,sys
             
def main():
    
    flag1=os.path.exists("data.txt")
    
    if flag1==True:
        fd=open("data.txt","r")
        data=fd.read()
        print(data)
        fd.close()
    else:
        print("File does not exist")    
        
if __name__=="__main__":
    main()