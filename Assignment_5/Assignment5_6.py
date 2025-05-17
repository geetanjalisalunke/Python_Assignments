def cel_to_f(no1):
   return (no1*9/5)+32

def main():
    
    print("Enter the Tempreture in Celsius")
    no=int(input())
    ans=cel_to_f(no)
    print(f"Tempreture in Fahrenheit :{ans}\u00B0F")
    
if __name__=="__main__":
    main()
    