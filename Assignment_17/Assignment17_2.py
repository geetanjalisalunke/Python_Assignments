import schedule,time,datetime

def Cur_Date_Time():
    print("Current Date and Time is :",datetime.datetime.now())
             
def main():
      
      schedule.every(1).minute.do(Cur_Date_Time)
      print("Application is waiting.........")
      while(True):
          schedule.run_pending()
          time.sleep(1)
        
if __name__=="__main__":
    main()