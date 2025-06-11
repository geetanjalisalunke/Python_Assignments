import os,sys
             
def main():
    
    flag1=os.path.exists("Student.txt")
    
    if flag1==True:
        fd=open("Student.txt","r")
        
        print(len(fd.readlines()))
        data=fd.read()
        #print(data)
        
        words=data.split()
        w_cnt=0
        for i in words:
            w_cnt=w_cnt+1
        print("Word Count is :",w_cnt)
        
        w_char=0
        for i in data:
            w_char=w_char+1
        print("Character Count is :",w_char)
       
        fd.close()
    else:
        print("File does not exist")    
        
if __name__=="__main__":
    main()