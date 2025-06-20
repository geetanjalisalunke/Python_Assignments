import sys
import schedule
import hashlib
import os
import time
import smtplib
from email.message import EmailMessage

def CalculateCheckSum(path,Blocksize=1024):
    fobj=open(path,'rb')
    buffer=fobj.read(Blocksize)
    hobj=hashlib.md5()
    
    while (len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(Blocksize)
        
    fobj.close()    
    return hobj.hexdigest()

def FindDuplicate(Dir_name) :
    
    flag=os.path.isabs(Dir_name)
    
    if flag==False:
        flag=os.path.abspath(Dir_name)
    
    flag=os.path.exists(Dir_name)
    
    if flag==False:
        print("The path is invalid.")
        exit()
        
    flag=os.path.isdir(Dir_name)
    
    if flag==False:
        print("Path is valid but target is not a Directory.")
        exit()
    
    Duplicate={}
    
    for FolderName,SubFolders,Files in os.walk(Dir_name):
        
        for file in Files:
            fname=os.path.join(FolderName,file)
            checksum=CalculateCheckSum(fname)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum]=[fname]
                
    return Duplicate

def Deletedup(path="Marvellous",mail='shivanjalis622@gmail.com')   :
    
    mydict=FindDuplicate(path)
    result=list(filter(lambda x:len(x)>1,mydict.values()))
    
    if os.path.exists('Demo'):
        pass
    else:
        os.mkdir("Demo")
        
    timestamp=time.ctime()
    Border='-'*80
    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    filename=os.path.join('Demo',filename)

    fobj = open(filename,"w")
    
    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("This is a Log File of Marvellous Automation Script."+"\n")
    fobj.write("This is a Directory Cleaner Script."+"\n")
    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This file is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")
    
    cnt=0
    cnt1=0
    total=0
    for value in result:
        total=total+len(value)
        for subval in value:
            cnt=cnt+1
            if cnt>1:
                os.remove(subval)
                print(subval)
                fobj.write(subval+"\n")
                cnt1=cnt1+1
        print("---------------------------------------------------")
        cnt=0 
    print("Deleted Files count is : ",cnt1)
    print("Total files scanned is :",total)   
    fobj.close()
    
    SendMail(mail,filename,total,cnt1)
    
def SendMail(mail,filename,total,cnt)    :
    
    log_file_path=filename

    msg = EmailMessage()
    msg['Subject'] = 'Log File Report'
    msg['From'] = 'geetanjalisalunke12@gmail.com'
    msg['To'] = mail
    content='Please find the attached log file.'+'\n'+'Starting time of Scanning is :'+str(time.ctime())+'\n'+'Total number of files scanned'+str(total)+'\n'+'Total number of Duplicated files is:'+str(cnt)+'\n'
    msg.set_content(content)

    fobj=open(log_file_path,'rb')
    data=fobj.read()
    file_name=fobj.name
    print(file_name)
    msg.add_attachment(data,maintype='application', subtype='octet-stream', filename=file_name)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'geetanjalisalunke12@gmail.com'
    password = 'qbkw cxrz uqyx onbg'  


    
    server = smtplib.SMTP(smtp_server, smtp_port)  
    server.starttls()                              
    server.login(username, password)               
    server.send_message(msg)                       
    server.quit() 

    print("Email with log file sent successfully.")