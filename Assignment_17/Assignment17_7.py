import schedule,time,datetime,shutil

def backup():
    
    time_stamp=str(datetime.datetime.now())
    File_name="backup_log.txt"
    
    shutil.copy("Marvellous.txt",File_name)
    fd=open(File_name,'a')
    fd.write(File_name+time_stamp+"\n")
    fd.close()
             
def main():
      schedule.every(2).seconds.do(backup)
      print("Application is waiting.........")
      
      while(True):
          schedule.run_pending()
          time.sleep(1)
        
if __name__=="__main__":
    main()