def DisplaySchedule(ch):
    
    if  ch=='a' or ch=='A':
        print("Your Exam at 7.00 AM")
    elif  ch=='b' or ch=='B':
        print("Your Exam at 8.30 AM")
    elif  ch=='c' or ch=='C':
        print("Your Exam at 9.20 AM")
    elif  ch=='d' or ch=='D':
        print("Your Exam at 10.30 AM")
    
        
def main():
    
    print("Enter Character")
    a=input()
    
    DisplaySchedule(a)
   
    
if __name__=="__main__":
    main()