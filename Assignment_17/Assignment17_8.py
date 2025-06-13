import schedule,time,datetime

def email():
   print("Checking email updates......")
             
def main():
      schedule.every(10).seconds.do(email)
      print("Application is waiting.........")
      
      while(True):
          schedule.run_pending()
          time.sleep(1)
        
if __name__=="__main__":
    main()