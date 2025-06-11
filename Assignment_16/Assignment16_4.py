import os,sys
             
def main():
    
    flag1=os.path.exists("Number.txt")
    
    if flag1==False:
        fd=open("Number.txt","w")
        print("Enter the 10 numbers")
        for no in range(10):
            num=input()
            fd.write(str(num)+'\n')
            
        fd.close()
        
    else:
        print("File exists")    
        
if __name__=="__main__":
    main()