import psutil,sys,os,time,json
import smtplib
from email.message import EmailMessage

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

    return path

def Send_mail(path):
    
    log_file_path=path

    msg = EmailMessage()
    msg['Subject'] = 'Log File Report'
    msg['From'] = 'geetanjalisalunke12@gmail.com'
    msg['To'] = 'shivanjalis622@gmail.com'
    msg.set_content('Please find the attached log file.')

    fobj=open(log_file_path,'rb')
    data=fobj.read()
    file_name=fobj.name
    print(file_name)
    msg.add_attachment(data,maintype='application', subtype='octet-stream', filename=file_name)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'geetanjalisalunke12@gmail.com'
    password = 'qbkw cxrz uqyx onbg'  # Use app password if 2FA is enabled

# Send the email with attachment
    
    server = smtplib.SMTP(smtp_server, smtp_port)  # Create SMTP connection
    server.starttls()                              # Secure it with TLS
    server.login(username, password)               # Login with email and App Password
    server.send_message(msg)                       # Send the email
    server.quit() 

    print("Email with log file sent successfully.")

    
def main():
    Dir_name=sys.argv[1]
    ret=ProcessDisplay(Dir_name)
    Send_mail(ret)

if __name__=="__main__":
    main()