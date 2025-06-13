import schedule,time,datetime

def Display():
    print("Do Coding....!")
             
def main():
      
      schedule.every(30).minutes.do(Display)
      print("Application is waiting.........")
      while(True):
          schedule.run_pending()
          time.sleep(1)
        
if __name__=="__main__":
    main()