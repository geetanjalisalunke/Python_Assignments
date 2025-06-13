import schedule,time,datetime

def Display1():
    print("Lunch Time...!")
    
def Display2():
    print("Wrap up work...")
             
def main():
      
      schedule.every().day.at("13:00").do(Display1)
      schedule.every().day.at("18:00").do(Display2)
      print("Application is waiting.........")
      
      while(True):
          schedule.run_pending()
          time.sleep(1)
        
if __name__=="__main__":
    main()