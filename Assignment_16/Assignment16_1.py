import os,sys
             
def main():
    
    flag1=os.path.exists("Student.txt")
    
    if flag1==False:
        fd=open("Student.txt","x")
        print("Enter the 5 students name")
        
        for i in range(5):
            S_name=input()
            fd.write(S_name+"\n")
        fd.close()
    else:
        print("File Already exists")    
        
if __name__=="__main__":
    main()